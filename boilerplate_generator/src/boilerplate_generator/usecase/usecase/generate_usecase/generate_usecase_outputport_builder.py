"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_outputport\
    import GenerateUsecaseOutputPort


@dataclass
class GenerateUsecaseOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: GenerateUsecaseOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_folders: List[str]
        fill the folders in the contract
    with_files: List[str]
        fill the files in the contract
    with_error:
        fill the possible usecase error
    build:
        build the final output contract

    """

    __output: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = GenerateUsecaseOutputPort()
        return self

    def with_folders(self, folders: List[str]):
        """ This function fill the folders in the contract

        Parameters:
        -----------
        folders: List[str]
            the folders of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.folders = folders
        return self

    def with_files(self, files: List[str]):
        """ This function fill the files in the contract

        Parameters:
        -----------
        files: List[str]
            the files of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.files = files
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> GenerateUsecaseOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        GenerateUsecaseOutputPort
            the contract filled

        """

        return self.__output
