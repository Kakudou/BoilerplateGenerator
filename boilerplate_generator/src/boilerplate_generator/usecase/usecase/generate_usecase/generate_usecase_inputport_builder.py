"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_inputport\
    import GenerateUsecaseInputPort


@dataclass
class GenerateUsecaseInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: GenerateUsecaseInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_usecase_name: str
        fill the usecase_name in the contract
    with_entity_name: str
        fill the entity_name in the contract
    with_entity_domain: str
        fill the entity_domain in the contract
    with_entity_attributes: List[str]
        fill the entity_attributes in the contract
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
        GenerateUsecaseInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = GenerateUsecaseInputPort()
        return self

    def with_usecase_name(self, usecase_name: str):
        """ This function fill the usecase_name in the contract

        Parameters:
        -----------
        usecase_name: str
            the usecase_name of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.usecase_name = usecase_name
        return self

    def with_entity_name(self, entity_name: str):
        """ This function fill the entity_name in the contract

        Parameters:
        -----------
        entity_name: str
            the entity_name of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.entity_name = entity_name
        return self

    def with_entity_domain(self, entity_domain: str):
        """ This function fill the entity_domain in the contract

        Parameters:
        -----------
        entity_domain: str
            the entity_domain of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.entity_domain = entity_domain
        return self

    def with_entity_attributes(self, entity_attributes: List[str]):
        """ This function fill the entity_attributes in the contract

        Parameters:
        -----------
        entity_attributes: List[str]
            the entity_attributes of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.entity_attributes = entity_attributes
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def with_project_path(self, project_path: str):
        """ This function fill the project_path in the contract

        Parameters:
        -----------
        project_path: str
            the project_path of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_path = project_path
        return self

    def with_project_types(self, project_types: List[str]):
        """ This function fill the project_types in the contract

        Parameters:
        -----------
        project_types: List[str]
            the project_types of the GenerateUsecase

        Returns:
        --------
        GenerateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_types = project_types
        return self

    def build(self) -> GenerateUsecaseInputPort:
        """ This function return the filled contract

        Returns:
        --------
        GenerateUsecaseInputPort
            the contract filled

        """

        return self.__input
