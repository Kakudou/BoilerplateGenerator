"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.read_entity.read_entity_outputport\
    import ReadEntityOutputPort


@dataclass
class ReadEntityOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ReadEntityOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_project_name: str
        fill the project_name in the contract
    with_name: str
        fill the name in the contract
    with_domain: str
        fill the domain in the contract
    with_attributes: List
        fill the attributes in the contract
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
        ReadEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ReadEntityOutputPort()
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

        self.__output.project_name = project_name
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

        self.__output.name = name
        return self

    def with_domain(self, domain: str):
        """ This function fill the domain in the contract

        Parameters:
        -----------
        domain: str
            the domain of the ReadEntity

        Returns:
        --------
        ReadEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.domain = domain
        return self

    def with_attributes(self, attributes: List):
        """ This function fill the attributes in the contract

        Parameters:
        -----------
        attributes: List
            the attributes of the ReadEntity

        Returns:
        --------
        ReadEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.attributes = attributes
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ReadEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ReadEntityOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        ReadEntityOutputPort
            the contract filled

        """

        return self.__output
