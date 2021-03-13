"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.list_project.list_project_inputport\
    import ListProjectInputPort


@dataclass
class ListProjectInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListProjectInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        ListProjectInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListProjectInputPort()
        return self

    def build(self) -> ListProjectInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListProjectInputPort
            the contract filled

        """

        return self.__input
