"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.read_entity.read_entity_inputport\
    import ReadEntityInputPort


@dataclass
class ReadEntityInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ReadEntityInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_project_name: str
        fill the project_name in the contract
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
        ReadEntityInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ReadEntityInputPort()
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the ReadEntity

        Returns:
        --------
        ReadEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the ReadEntity

        Returns:
        --------
        ReadEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.name = name
        return self

    def build(self) -> ReadEntityInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ReadEntityInputPort
            the contract filled

        """

        return self.__input
