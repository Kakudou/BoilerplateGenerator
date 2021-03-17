"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.delete_usecase.delete_usecase_outputport\
    import DeleteUsecaseOutputPort


@dataclass
class DeleteUsecaseOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: DeleteUsecaseOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_deleted: bool
        fill the deleted in the contract
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
        DeleteUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = DeleteUsecaseOutputPort()
        return self

    def with_deleted(self, deleted: bool):
        """ This function fill the deleted in the contract

        Parameters:
        -----------
        deleted: bool
            the deleted of the DeleteUsecase

        Returns:
        --------
        DeleteUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.deleted = deleted
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        DeleteUsecaseOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> DeleteUsecaseOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        DeleteUsecaseOutputPort
            the contract filled

        """

        return self.__output
