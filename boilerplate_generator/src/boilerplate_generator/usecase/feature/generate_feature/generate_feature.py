"""This module is the core logic to create a Entity"""
import os

from dataclasses\
    import dataclass
from typing\
    import Any
from jinja2\
    import Environment, FileSystemLoader

from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.generate_feature.generate_feature_inputport\
    import GenerateFeatureInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.generate_feature.generate_feature_outputport_builder\
    import GenerateFeatureOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.generate_feature.generate_feature_outputport\
    import GenerateFeatureOutputPort

from boilerplate_generator.src.boilerplate_generator.entity.\
    project.project\
    import Project
from boilerplate_generator.src.boilerplate_generator.entity.\
    feature.feature\
    import Feature


@dataclass
class GenerateFeature:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: GenerateFeatureOutputPort
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
        the usecase_container utils class give it the good implemented_gateway

        Parameters:
        -----------
        implemented_gateway:
            The implemented_gateway for the storage engine we want
        """

        self.gateway = implemented_gateway
        self.builder = GenerateFeatureOutputPortBuilder()

    def execute(self, inputp: GenerateFeatureInputPort) -> GenerateFeatureOutputPort:
        """This function will from the inputport create a Feature
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: GenerateFeatureInputPort
            the inputport who come from the adapter

        Returns:
        --------
        GenerateFeatureOutputPort:
            The output contract

        """

        executed = False
        feature = None

        project_name = inputp.project_name
        feature_name = inputp.feature_name
        force = inputp.force

        identifier = (feature_name, project_name)
        feature = self.gateway.find_by_identifier(identifier)

        project = Project()
        project.name = project_name
        project.path = inputp.project_path
        project.types = inputp.project_types
        dest_path = f"{project.path}/{project.name}"

        folders = [
            f"{dest_path}/{project.snakename}/features/{project.snakename}/",
            f"{dest_path}/{project.snakename}/tests/features/{project.snakename}/",
        ]

        files = [
            f"{dest_path}/{project.snakename}/features/{project.snakename}/{feature.snakename}.feature",
            f"{dest_path}/{project.snakename}/tests/features/{project.snakename}/test_{feature.snakename}.py",
        ]

        created_folders = []
        for folder in folders:
            created = self._create_folder(folder)
            if created:
                created_folders.append(folder)

        created_files = []
        for file in files:
            created = self._create_file(file, project, feature, force)
            if created:
                created_files.append(file)

        executed = True

        if executed:
            self.__output = self.builder.create()\
                                .with_folders(created_folders)\
                                .with_files(created_files)\
                                .build()

        elif not executed and feature is None:
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
    def _create_file(path: str, project: Project, feature: Feature, force) -> bool:
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

            filename = path.split('/')[-1].replace(feature.snakename, "feature")

            filetmpl = env.get_template(f"./templates/{filename}.j2")
            filetmpl.stream(project=project, feature=feature).dump(f"{path}")
            created = True
        return created
