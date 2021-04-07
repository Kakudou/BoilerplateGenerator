""" This module use the usecase DeleteUsecase"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.delete_usecase.delete_usecase_inputport_builder\
    import DeleteUsecaseInputPortBuilder


class DeleteUsecaseAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase DeleteUsecase.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into DeleteUsecaseInputPort
        with the use of DeleteUsecaseInputPortBuilder.
        Then this contract will be gave to DeleteUsecase usecase.
        In return we should obtain the contract DeleteUsecaseOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the usecase
            project_name: str
                The name of the project

        Returns:
        --------
        DeleteUsecase_oc
            the output contract of the usecase DeleteUsecase

        """

        sanitize_name = inputs["name"]
        sanitize_project_name = inputs["project_name"]

        delete_usecase_icb = DeleteUsecaseInputPortBuilder()
        delete_usecase_ic = delete_usecase_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_project_name(sanitize_project_name)\
            .build()

        delete_usecase_oc = Container\
            .get_usecase_repo("DeleteUsecase", storage_engine)\
            .execute(delete_usecase_ic)

        return delete_usecase_oc
