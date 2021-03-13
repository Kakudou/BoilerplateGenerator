"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.read_project.read_project_outputport\
    import ReadProjectOutputPort


@dataclass
class ReadProjectOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ReadProjectOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_name: str
        fill the name in the contract
    with_path: str
        fill the path in the contract
    with_types: List[str]
        fill the types in the contract
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
        ReadProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ReadProjectOutputPort()
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

        self.__output.name = name
        return self

    def with_path(self, path: str):
        """ This function fill the path in the contract

        Parameters:
        -----------
        path: str
            the path of the ReadProject

        Returns:
        --------
        ReadProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.path = path
        return self

    def with_types(self, types: List[str]):
        """ This function fill the types in the contract

        Parameters:
        -----------
        types: List[str]
            the types of the ReadProject

        Returns:
        --------
        ReadProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.types = types
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ReadProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ReadProjectOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        ReadProjectOutputPort
            the contract filled

        """

        return self.__output
