"""This module is the core logic to create a Entity"""
import os

from dataclasses\
    import dataclass
from typing\
    import Any
from jinja2\
    import Environment, FileSystemLoader

from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.generate_entity.generate_entity_inputport\
    import GenerateEntityInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.generate_entity.generate_entity_outputport_builder\
    import GenerateEntityOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.generate_entity.generate_entity_outputport\
    import GenerateEntityOutputPort

from boilerplate_generator.src.boilerplate_generator.entity.\
    project.project\
    import Project
from boilerplate_generator.src.boilerplate_generator.entity.\
    entity.entity\
    import Entity


@dataclass
class GenerateEntity:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: GenerateEntityOutputPort
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
        self.builder = GenerateEntityOutputPortBuilder()

    def execute(self, inputp: GenerateEntityInputPort) -> GenerateEntityOutputPort:
        """This function will from the inputport create a Entity
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: GenerateEntityInputPort
            the inputport who come from the adapter

        Returns:
        --------
        GenerateEntityOutputPort:
            The output contract

        """

        executed = False
        entity = None

        project_name = inputp.project_name
        entity_name = inputp.entity_name
        force = inputp.force

        identifier = (project_name, entity_name)
        entity = self.gateway.find_by_identifier(identifier)

        project = Project()
        project.name = project_name
        project.path = inputp.project_path
        project.types = inputp.project_types
        dest_path = f"{project.path}/{project.name}"

        folders = [
            f"{dest_path}/{project.snakename}/src/app/dto/{entity.snakedomain}/",
            f"{dest_path}/{project.snakename}/src/app/repository/inmemory/{entity.snakedomain}/",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/entity/{entity.snakedomain}/",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/gateway/{entity.snakedomain}/",
        ]

        files = [
            f"{dest_path}/{project.snakename}/src/app/dto/{entity.snakedomain}/{entity.snakename}_dto.py",
            f"{dest_path}/{project.snakename}/src/app/repository/inmemory/{entity.snakedomain}/{entity.snakename}_inmemory_repository.py",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/entity/{entity.snakedomain}/{entity.snakename}.py",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/gateway/{entity.snakedomain}/{entity.snakename}_gateway.py",
        ]
        if len(project.types) != 0:
            for project_type in project.types:
                files.append(f"{dest_path}/{project.snakename}/src/app/{project_type}/entity_view/{entity.snakedomain}/{entity.snakename}_view.py")
                folders.append(f"{dest_path}/{project.snakename}/src/app/{project_type}/entity_view/{entity.snakedomain}/")

        created_folders = []
        for folder in folders:
            created = self._create_folder(folder)
            if created:
                created_folders.append(folder)

        created_files = []
        for file in files:
            created = self._create_file(file, project, entity, force)
            if created:
                created_files.append(file)

        executed = True

        if executed:
            self.__output = self.builder.create()\
                                .with_folders(created_folders)\
                                .with_files(created_files)\
                                .build()

        elif not executed and entity is None:
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
    def _create_file(path: str, project: Project, entity: Entity, force) -> bool:
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
        if not os.path.isfile(path) or force:
            env = Environment(loader=FileSystemLoader("boilerplate_generator"),
                              trim_blocks=True, lstrip_blocks=True)

            filename = path.split('/')[-1].replace(entity.snakename, "entity")

            filetmpl = env.get_template(f"./templates/{filename}.j2")
            filetmpl.stream(project=project, entity=entity).dump(f"{path}")
            created = True
        return created
