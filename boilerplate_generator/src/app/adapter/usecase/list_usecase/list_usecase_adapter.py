""" This module use the usecase ListUsecase"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase.list_usecase_inputport_builder\
    import ListUsecaseInputPortBuilder


class ListUsecaseAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ListUsecase.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ListUsecaseInputPort
        with the use of ListUsecaseInputPortBuilder.
        Then this contract will be gave to ListUsecase usecase.
        In return we should obtain the contract ListUsecaseOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:

        Returns:
        --------
        ListUsecase_oc
            the output contract of the usecase ListUsecase

        """

        sanitize_project_name = inputs["project_name"]

        list_usecase_icb = ListUsecaseInputPortBuilder()
        list_usecase_ic = list_usecase_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .build()

        list_usecase_oc = UsecaseContainer\
            .get("ListUsecase", storage_engine)\
            .execute(list_usecase_ic)

        return list_usecase_oc
