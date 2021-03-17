"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase.list_usecase_inputport\
    import ListUsecaseInputPort


@dataclass
class ListUsecaseInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListUsecaseInputPort
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
        ListUsecaseInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListUsecaseInputPort()
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the ListUsecase

        Returns:
        --------
        ListUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def build(self) -> ListUsecaseInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListUsecaseInputPort
            the contract filled

        """

        return self.__input
