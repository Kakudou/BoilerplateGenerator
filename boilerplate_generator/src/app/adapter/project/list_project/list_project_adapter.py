""" This module use the usecase ListProject"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.list_project.list_project_inputport_builder\
    import ListProjectInputPortBuilder


class ListProjectAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ListProject.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ListProjectInputPort
        with the use of ListProjectInputPortBuilder.
        Then this contract will be gave to ListProject usecase.
        In return we should obtain the contract ListProjectOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:

        Returns:
        --------
        ListProject_oc
            the output contract of the usecase ListProject

        """

        list_project_icb = ListProjectInputPortBuilder()
        list_project_ic = list_project_icb\
            .create()\
            .build()

        list_project_oc = Container\
            .get_usecase("ListProject", storage_engine)\
            .execute(list_project_ic)

        return list_project_oc
