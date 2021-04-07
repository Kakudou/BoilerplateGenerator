""" This module use the usecase UpdateProject"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.update_project.update_project_inputport_builder\
    import UpdateProjectInputPortBuilder


class UpdateProjectAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase UpdateProject.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into UpdateProjectInputPort
        with the use of UpdateProjectInputPortBuilder.
        Then this contract will be gave to UpdateProject usecase.
        In return we should obtain the contract UpdateProjectOutputPort

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
        UpdateProject_oc
            the output contract of the usecase UpdateProject

        """

        sanitize_name = inputs["name"]
        sanitize_path = inputs["path"]
        sanitize_types = inputs["types"]

        update_project_icb = UpdateProjectInputPortBuilder()
        update_project_ic = update_project_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_path(sanitize_path)\
            .with_types(sanitize_types)\
            .build()

        update_project_oc = Container\
            .get_usecase_repo("UpdateProject", storage_engine)\
            .execute(update_project_ic)

        return update_project_oc
