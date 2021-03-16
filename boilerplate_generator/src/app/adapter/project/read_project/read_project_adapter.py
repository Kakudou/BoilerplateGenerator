""" This module use the usecase ReadProject"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.read_project.read_project_inputport_builder\
    import ReadProjectInputPortBuilder


class ReadProjectAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ReadProject.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ReadProjectInputPort
        with the use of ReadProjectInputPortBuilder.
        Then this contract will be gave to ReadProject usecase.
        In return we should obtain the contract ReadProjectOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the project

        Returns:
        --------
        ReadProject_oc
            the output contract of the usecase ReadProject

        """

        sanitize_name = inputs["name"]

        read_project_icb = ReadProjectInputPortBuilder()
        read_project_ic = read_project_icb\
            .create()\
            .with_name(sanitize_name)\
            .build()

        read_project_oc = UsecaseContainer\
            .get("ReadProject", storage_engine)\
            .execute(read_project_ic)

        return read_project_oc
