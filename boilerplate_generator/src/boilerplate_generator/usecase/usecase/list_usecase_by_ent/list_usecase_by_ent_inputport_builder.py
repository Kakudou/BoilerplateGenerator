"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase_by_ent.list_usecase_by_ent_inputport\
    import ListUsecaseByEntInputPort


@dataclass
class ListUsecaseByEntInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListUsecaseByEntInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_project_name: str
        fill the project_name in the contract
    with_entity_name: str
        fill the entity_name in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        ListUsecaseByEntInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListUsecaseByEntInputPort()
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the ListUsecaseByEnt

        Returns:
        --------
        ListUsecaseByEntOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def with_entity_name(self, entity_name: str):
        """ This function fill the entity_name in the contract

        Parameters:
        -----------
        entity_name: str
            the entity_name of the ListUsecaseByEnt

        Returns:
        --------
        ListUsecaseByEntOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.entity_name = entity_name
        return self

    def build(self) -> ListUsecaseByEntInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListUsecaseByEntInputPort
            the contract filled

        """

        return self.__input
