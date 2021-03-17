"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.update_usecase.update_usecase_outputport\
    import UpdateUsecaseOutputPort


@dataclass
class UpdateUsecaseOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: UpdateUsecaseOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_name: str
        fill the name in the contract
    with_description: str
        fill the description in the contract
    with_type_: str
        fill the type_ in the contract
    with_entity_name: str
        fill the entity_name in the contract
    with_project_name: str
        fill the project_name in the contract
    with_input_attrs: List
        fill the input_attrs in the contract
    with_output_attrs: List
        fill the output_attrs in the contract
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
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = UpdateUsecaseOutputPort()
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the UpdateUsecase

        Returns:
        --------
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.name = name
        return self

    def with_description(self, description: str):
        """ This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the UpdateUsecase

        Returns:
        --------
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.description = description
        return self

    def with_type_(self, type_: str):
        """ This function fill the type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the UpdateUsecase

        Returns:
        --------
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.type_ = type_
        return self

    def with_entity_name(self, entity_name: str):
        """ This function fill the entity_name in the contract

        Parameters:
        -----------
        entity_name: str
            the entity_name of the UpdateUsecase

        Returns:
        --------
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.entity_name = entity_name
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the UpdateUsecase

        Returns:
        --------
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.project_name = project_name
        return self

    def with_input_attrs(self, input_attrs: List):
        """ This function fill the input_attrs in the contract

        Parameters:
        -----------
        input_attrs: List
            the input_attrs of the UpdateUsecase

        Returns:
        --------
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.input_attrs = input_attrs
        return self

    def with_output_attrs(self, output_attrs: List):
        """ This function fill the output_attrs in the contract

        Parameters:
        -----------
        output_attrs: List
            the output_attrs of the UpdateUsecase

        Returns:
        --------
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.output_attrs = output_attrs
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        UpdateUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> UpdateUsecaseOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        UpdateUsecaseOutputPort
            the contract filled

        """

        return self.__output
