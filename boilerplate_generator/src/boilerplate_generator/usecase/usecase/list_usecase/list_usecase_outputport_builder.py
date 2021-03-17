"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase.list_usecase_outputport\
    import ListUsecaseOutputPort


@dataclass
class ListUsecaseOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListUsecaseOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_all_usecases: List[str]
        fill the all_usecases in the contract
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
        ListUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListUsecaseOutputPort()
        return self

    def with_all_usecases(self, all_usecases: List[str]):
        """ This function fill the all_usecases in the contract

        Parameters:
        -----------
        all_usecases: List[str]
            the all_usecases of the ListUsecase

        Returns:
        --------
        ListUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.all_usecases = all_usecases
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ListUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListUsecaseOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListUsecaseOutputPort
            the contract filled

        """

        return self.__output
