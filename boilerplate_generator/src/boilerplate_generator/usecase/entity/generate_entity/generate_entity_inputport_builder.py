"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.generate_entity.generate_entity_inputport\
    import GenerateEntityInputPort


@dataclass
class GenerateEntityInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: GenerateEntityInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_entity_name: str
        fill the entity_name in the contract
    with_force: bool
        fill the force in the contract
    with_project_name: str
        fill the project_name in the contract
    with_project_path: str
        fill the project_path in the contract
    with_project_types: List[str]
        fill the project_types in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        GenerateEntityInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = GenerateEntityInputPort()
        return self

    def with_entity_name(self, entity_name: str):
        """ This function fill the entity_name in the contract

        Parameters:
        -----------
        entity_name: str
            the entity_name of the GenerateEntity

        Returns:
        --------
        GenerateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.entity_name = entity_name
        return self

    def with_force(self, force: bool):
        """ This function fill the force in the contract

        Parameters:
        -----------
        force: bool
            the force of the GenerateEntity

        Returns:
        --------
        GenerateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.force = force
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the GenerateEntity

        Returns:
        --------
        GenerateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def with_project_path(self, project_path: str):
        """ This function fill the project_path in the contract

        Parameters:
        -----------
        project_path: str
            the project_path of the GenerateEntity

        Returns:
        --------
        GenerateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_path = project_path
        return self

    def with_project_types(self, project_types: List[str]):
        """ This function fill the project_types in the contract

        Parameters:
        -----------
        project_types: List[str]
            the project_types of the GenerateEntity

        Returns:
        --------
        GenerateEntityOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_types = project_types
        return self

    def build(self) -> GenerateEntityInputPort:
        """ This function return the filled contract

        Returns:
        --------
        GenerateEntityInputPort
            the contract filled

        """

        return self.__input
