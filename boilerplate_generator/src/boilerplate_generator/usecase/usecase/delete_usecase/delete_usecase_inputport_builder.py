"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.delete_usecase.delete_usecase_inputport\
    import DeleteUsecaseInputPort


@dataclass
class DeleteUsecaseInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: DeleteUsecaseInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_name: str
        fill the name in the contract
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
        DeleteUsecaseInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = DeleteUsecaseInputPort()
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the DeleteUsecase

        Returns:
        --------
        DeleteUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.name = name
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the DeleteUsecase

        Returns:
        --------
        DeleteUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def build(self) -> DeleteUsecaseInputPort:
        """ This function return the filled contract

        Returns:
        --------
        DeleteUsecaseInputPort
            the contract filled

        """

        return self.__input
