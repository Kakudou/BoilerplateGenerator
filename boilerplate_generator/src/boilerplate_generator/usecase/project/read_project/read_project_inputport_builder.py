"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.read_project.read_project_inputport\
    import ReadProjectInputPort


@dataclass
class ReadProjectInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ReadProjectInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_name: str
        fill the name in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        ReadProjectInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ReadProjectInputPort()
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the ReadProject

        Returns:
        --------
        ReadProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.name = name
        return self

    def build(self) -> ReadProjectInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ReadProjectInputPort
            the contract filled

        """

        return self.__input
