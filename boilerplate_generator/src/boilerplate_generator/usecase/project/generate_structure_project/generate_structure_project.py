"""This module is the core logic to create a Entity"""
import os

from dataclasses\
    import dataclass
from typing\
    import Any
from jinja2\
    import Environment, FileSystemLoader

from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.generate_structure_project.generate_structure_project_inputport\
    import GenerateStructureProjectInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.generate_structure_project.generate_structure_project_outputport_builder\
    import GenerateStructureProjectOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.generate_structure_project.generate_structure_project_outputport\
    import GenerateStructureProjectOutputPort

from boilerplate_generator.src.boilerplate_generator.entity.project.project\
    import Project


@dataclass
class GenerateStructureProject:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: GenerateStructureProjectOutputPort
        is the outputport information who gonna travel to the adapter

    Functions:
    ----------
    __init__:
        classical constructor
    execute:
        execute the usecase logic

    """

    __output: Any = None

    def __init__(self, implemented_gateway):
        """This function is the constructor particularity:
        the container utils class give it the good implemented_gateway

        Parameters:
        -----------
        implemented_gateway:
            The implemented_gateway for the storage engine we want
        """

        self.gateway = implemented_gateway
        self.builder = GenerateStructureProjectOutputPortBuilder()

    def execute(self, inputp: GenerateStructureProjectInputPort) -> GenerateStructureProjectOutputPort:
        """This function will from the inputport create a Project
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: GenerateStructureProjectInputPort
            the inputport who come from the adapter

        Returns:
        --------
        GenerateStructureProjectOutputPort:
            The output contract

        """

        executed = False
        project = None

        project_name = inputp.project_name
        force = inputp.force

        identifier = (project_name)

        project = self.gateway.find_by_identifier(identifier)

        dest_path = f"{project.path}/{project.name}"

        folders = [
            f"{dest_path}",
            f"{dest_path}/{project.snakename}",
            f"{dest_path}/{project.snakename}/constraints",
            f"{dest_path}/{project.snakename}/constraints/{project.snakename}",
            f"{dest_path}/{project.snakename}/features",
            f"{dest_path}/{project.snakename}/features/{project.snakename}",
            f"{dest_path}/{project.snakename}/src",
            f"{dest_path}/{project.snakename}/src/app",
            f"{dest_path}/{project.snakename}/src/app/adapter",
            f"{dest_path}/{project.snakename}/src/app/dto",
            f"{dest_path}/{project.snakename}/src/app/repository",
            f"{dest_path}/{project.snakename}/src/app/repository/inmemory",
            f"{dest_path}/{project.snakename}/src/{project.snakename}",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/entity",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/gateway",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase",
            f"{dest_path}/{project.snakename}/src/utils",
            f"{dest_path}/{project.snakename}/tests",
            f"{dest_path}/{project.snakename}/tests/constraints",
            f"{dest_path}/{project.snakename}/tests/constraints/{project.snakename}",
            f"{dest_path}/{project.snakename}/tests/features",
            f"{dest_path}/{project.snakename}/tests/features/{project.snakename}",
        ]

        files = [
            f"{dest_path}/.gitignore",
            f"{dest_path}/LICENSE",
            f"{dest_path}/README.md",
            f"{dest_path}/requirements",
            f"{dest_path}/setup.py",
            f"{dest_path}/{project.snakename}/src/__init__.py",
            f"{dest_path}/{project.snakename}/src/app/repository/inmemory/inmemory_persist.py",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/gateway/abstract_gateway.py",
            f"{dest_path}/{project.snakename}/src/utils/container.py",
            f"{dest_path}/{project.snakename}/src/utils/debug.py",
            f"{dest_path}/{project.snakename}/src/utils/singleton.py",
            f"{dest_path}/{project.snakename}/tests/factory.py",
        ]

        if len(project.types) != 0:
            for project_type in project.types:
                folders.append(f"{dest_path}/{project.snakename}/constraints/{project_type}"),
                folders.append(f"{dest_path}/{project.snakename}/tests/constraints/{project_type}"),
                folders.append(f"{dest_path}/{project.snakename}/features/{project_type}"),
                folders.append(f"{dest_path}/{project.snakename}/tests/features/{project_type}"),
                folders.append(f"{dest_path}/{project.snakename}/src/app/{project_type}")
                folders.append(f"{dest_path}/{project.snakename}/src/app/{project_type}/entity_view")
                folders.append(f"{dest_path}/{project.snakename}/src/app/{project_type}/view")

        created_folders = []
        for folder in folders:
            created = self._create_folder(folder)
            if created:
                created_folders.append(folder)

        created_files = []
        for file in files:
            created = self._create_file(file, project, force)
            if created:
                created_files.append(file)

        executed = True

        if executed:
            self.__output = self.builder.create()\
                                .with_folders(created_folders)\
                                .with_files(created_files)\
                                .build()

        elif not executed and project is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output

    @staticmethod
    def _create_folder(path: str) -> bool:
        """This function will be used to create a folder if it doesn't exists

        Parameters:
        -----------
        path: str
            Contains the path that will be created if it doesn't exists

        Return:
        -------
        bool
            True if  the folder has been created
        """

        created = False
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                if not os.path.exists(f"{path}/__init__.py"):
                    os.mknod(f"{path}/__init__.py")
                created = True
            except PermissionError as err:
                print(f"can't create folder at {path}: {err}")
                raise PermissionError
        return created

    @staticmethod
    def _create_file(path: str, project: Project, force) -> bool:
        """This function will be used to create a file if it doesn't exists
        based on a jinja2 template

        Parameters:
        -----------
        path: str
            Contains the path file that will be created if it doesn't exists

        Return:
        -------
        bool
            True if  the file has been created
        """

        created = False
        if not os.path.isfile(path) or force or "__init__" in path :
            env = Environment(loader=FileSystemLoader("boilerplate_generator"),
                              trim_blocks=True, lstrip_blocks=True)

            filename = path.split('/')[-1].replace(project.snakename, "project")

            filetmpl = env.get_template(f"./templates/{filename}.j2")
            filetmpl.stream(project=project).dump(f"{path}")
            created = True
        return created
