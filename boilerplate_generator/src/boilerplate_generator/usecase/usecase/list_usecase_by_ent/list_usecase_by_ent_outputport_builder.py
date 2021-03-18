"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase_by_ent.list_usecase_by_ent_outputport\
    import ListUsecaseByEntOutputPort


@dataclass
class ListUsecaseByEntOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListUsecaseByEntOutputPort
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
        ListUsecaseByEntOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListUsecaseByEntOutputPort()
        return self

    def with_all_usecases(self, all_usecases: List[str]):
        """ This function fill the all_usecases in the contract

        Parameters:
        -----------
        all_usecases: List[str]
            the all_usecases of the ListUsecaseByEnt

        Returns:
        --------
        ListUsecaseByEntOutputPortBuilder
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
        ListUsecaseByEntOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListUsecaseByEntOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListUsecaseByEntOutputPort
            the contract filled

        """

        return self.__output
