""" This module use the usecase CreateProject"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.create_project.create_project_inputport_builder\
    import CreateProjectInputPortBuilder


class CreateProjectAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase CreateProject.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into CreateProjectInputPort
        with the use of CreateProjectInputPortBuilder.
        Then this contract will be gave to CreateProject usecase.
        In return we should obtain the contract CreateProjectOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the project
            path: str
                The path of the project
            types: List[str]
                The type of the project

        Returns:
        --------
        CreateProject_oc
            the output contract of the usecase CreateProject

        """

        sanitize_name = inputs["name"]
        sanitize_path = inputs["path"]
        sanitize_types = inputs["types"]

        create_project_icb = CreateProjectInputPortBuilder()
        create_project_ic = create_project_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_path(sanitize_path)\
            .with_types(sanitize_types)\
            .build()

        create_project_oc = Container\
            .get_usecase_repo("CreateProject", storage_engine)\
            .execute(create_project_ic)

        return create_project_oc
