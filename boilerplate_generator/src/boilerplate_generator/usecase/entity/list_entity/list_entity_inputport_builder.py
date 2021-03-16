"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.list_entity.list_entity_inputport\
    import ListEntityInputPort


@dataclass
class ListEntityInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListEntityInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_project_name: str
        fill the project_name in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        ListEntityInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListEntityInputPort()
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the ListEntity

        Returns:
        --------
        ListEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def build(self) -> ListEntityInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListEntityInputPort
            the contract filled

        """

        return self.__input
