"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.list_entity.list_entity_outputport\
    import ListEntityOutputPort


@dataclass
class ListEntityOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListEntityOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_all_entitys: List[str]
        fill the all_entitys in the contract
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
        ListEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListEntityOutputPort()
        return self

    def with_all_entitys(self, all_entitys: List[str]):
        """ This function fill the all_entitys in the contract

        Parameters:
        -----------
        all_entitys: List[str]
            the all_entitys of the ListEntity

        Returns:
        --------
        ListEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.all_entitys = all_entitys
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ListEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListEntityOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListEntityOutputPort
            the contract filled

        """

        return self.__output
