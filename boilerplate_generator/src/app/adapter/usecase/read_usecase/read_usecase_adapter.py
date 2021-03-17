""" This module use the usecase ReadUsecase"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.read_usecase.read_usecase_inputport_builder\
    import ReadUsecaseInputPortBuilder


class ReadUsecaseAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ReadUsecase.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ReadUsecaseInputPort
        with the use of ReadUsecaseInputPortBuilder.
        Then this contract will be gave to ReadUsecase usecase.
        In return we should obtain the contract ReadUsecaseOutputPort

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
        ReadUsecase_oc
            the output contract of the usecase ReadUsecase

        """

        sanitize_name = inputs["name"]

        sanitize_project_name = inputs["project_name"]

        read_usecase_icb = ReadUsecaseInputPortBuilder()
        read_usecase_ic = read_usecase_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_project_name(sanitize_project_name)\
            .build()

        read_usecase_oc = UsecaseContainer\
            .get("ReadUsecase", storage_engine)\
            .execute(read_usecase_ic)

        return read_usecase_oc
