"""This module is the core logic to create a Entity"""
import os

from dataclasses\
    import dataclass
from typing\
    import Any
from jinja2\
    import Environment, FileSystemLoader

from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_inputport\
    import GenerateUsecaseInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_outputport_builder\
    import GenerateUsecaseOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_outputport\
    import GenerateUsecaseOutputPort

from boilerplate_generator.src.boilerplate_generator.entity.\
    project.project\
    import Project
from boilerplate_generator.src.boilerplate_generator.entity.\
    entity.entity\
    import Entity
from boilerplate_generator.src.boilerplate_generator.entity.\
    usecase.usecase\
    import Usecase


@dataclass
class GenerateUsecase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: GenerateUsecaseOutputPort
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
        self.builder = GenerateUsecaseOutputPortBuilder()

    def execute(self, inputp: GenerateUsecaseInputPort) -> GenerateUsecaseOutputPort:
        """This function will from the inputport create a Usecase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: GenerateUsecaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        GenerateUsecaseOutputPort:
            The output contract

        """

        executed = False
        usecase = None

        project_name = inputp.project_name
        entity_name = inputp.entity_name
        usecase_name = inputp.usecase_name
        force = inputp.force

        identifier = (usecase_name, project_name)
        usecase = self.gateway.find_by_identifier(identifier)

        entity = Entity()
        entity.name = entity_name
        entity.domain = inputp.entity_domain
        entity.attributes = inputp.entity_attributes

        project = Project()
        project.name = project_name
        project.path = inputp.project_path
        project.types = inputp.project_types
        dest_path = f"{project.path}/{project.name}"

        if "Create" == usecase.type_:
            usecase.input_attrs = usecase.output_attrs = entity.attributes
        elif "Read" == usecase.type_:
            usecase.input_attrs = []
            for attr in entity.attributes:
                if attr["identifier"]:
                    usecase.input_attrs.append(attr)
            usecase.output_attrs = entity.attributes
        elif "Update" == usecase.type_:
            usecase.input_attrs = usecase.output_attrs = entity.attributes
        elif "Delete" == usecase.type_:
            usecase.input_attrs = []
            for attr in entity.attributes:
                if attr["identifier"]:
                    usecase.input_attrs.append(attr)
            usecase.output_attrs = []
            usecase.output_attrs.append({
                "name": "deleted",
                "description": "Flag true if deleted",
                "type": "bool",
            })
        elif "List" == usecase.type_:
            usecase.input_attrs = []
            usecase.output_attrs = []
            usecase.output_attrs.append({
                "name": f"all_{entity.snakename}s",
                "description": f"List of all {entity.snakename}s",
                "type": "List[str]",
            })

        folders = [
            f"{dest_path}/{project.snakename}/src/app/adapter/{entity.snakedomain}/{usecase.snakename}",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase/",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase/{entity.snakedomain}",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase/{entity.snakedomain}/{usecase.snakename}"
        ]

        files = [
            f"{dest_path}/{project.snakename}/src/app/adapter/{entity.snakedomain}/{usecase.snakename}/{usecase.snakename}_adapter.py",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase/{entity.snakedomain}/{usecase.snakename}/{usecase.snakename}.py",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase/{entity.snakedomain}/{usecase.snakename}/{usecase.snakename}_inputport.py",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase/{entity.snakedomain}/{usecase.snakename}/{usecase.snakename}_inputport_builder.py",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase/{entity.snakedomain}/{usecase.snakename}/{usecase.snakename}_outputport.py",
            f"{dest_path}/{project.snakename}/src/{project.snakename}/usecase/{entity.snakedomain}/{usecase.snakename}/{usecase.snakename}_outputport_builder.py"
        ]

        created_folders = []
        for folder in folders:
            created = self._create_folder(folder)
            if created:
                created_folders.append(folder)

        created_files = []
        for file in files:
            created = self._create_file(file, project, entity, usecase, force)
            if created:
                created_files.append(file)

        executed = True

        if executed:
            self.__output = self.builder.create()\
                                .with_folders(created_folders)\
                                .with_files(created_files)\
                                .build()

        elif not executed and usecase is None:
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
                created = True
            except PermissionError as err:
                print(f"can't create folder at {path}: {err}")
                raise PermissionError
        return created

    @staticmethod
    def _create_file(path: str, project: Project, entity: Entity, usecase: Usecase, force) -> bool:
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

            filename = path.split('/')[-1].replace(usecase.snakename, "usecase")

            filetmpl = env.get_template(f"./templates/{filename}.j2")
            filetmpl.stream(project=project, entity=entity, usecase=usecase).dump(f"{path}")
            created = True
        return created
