"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.create_entity.create_entity_inputport\
    import CreateEntityInputPort


@dataclass
class CreateEntityInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: CreateEntityInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_project_name: str
        fill the project_name in the contract
    with_name: str
        fill the name in the contract
    with_domain: str
        fill the domain in the contract
    with_attributes: List
        fill the attributes in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        CreateEntityInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = CreateEntityInputPort()
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the CreateEntity

        Returns:
        --------
        CreateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the CreateEntity

        Returns:
        --------
        CreateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.name = name
        return self

    def with_domain(self, domain: str):
        """ This function fill the domain in the contract

        Parameters:
        -----------
        domain: str
            the domain of the CreateEntity

        Returns:
        --------
        CreateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.domain = domain
        return self

    def with_attributes(self, attributes: List):
        """ This function fill the attributes in the contract

        Parameters:
        -----------
        attributes: List
            the attributes of the CreateEntity

        Returns:
        --------
        CreateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.attributes = attributes
        return self

    def build(self) -> CreateEntityInputPort:
        """ This function return the filled contract

        Returns:
        --------
        CreateEntityInputPort
            the contract filled

        """

        return self.__input