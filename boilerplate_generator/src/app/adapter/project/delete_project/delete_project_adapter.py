""" This module use the usecase DeleteProject"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.delete_project.delete_project_inputport_builder\
    import DeleteProjectInputPortBuilder


class DeleteProjectAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: classmethod
        will consume the usecase DeleteProject.

    """

    @classmethod
    def execute(cls, inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into DeleteProjectInputPort
        with the use of DeleteProjectInputPortBuilder.
        Then this contract will be gave to DeleteProject usecase.
        In return we should obtain the contract DeleteProjectOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the project

        Returns:
        --------
        DeleteProject_oc
            the output contract of the usecase DeleteProject

        """

        sanitize_name = inputs["name"]

        delete_project_icb = DeleteProjectInputPortBuilder()
        delete_project_ic = delete_project_icb\
            .create()\
            .with_name(sanitize_name)\
            .build()

        delete_project_oc = UsecaseContainer\
            .get("DeleteProject", storage_engine)\
            .execute(delete_project_ic)

        return delete_project_oc
