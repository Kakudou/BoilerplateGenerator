"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.delete_constraint.delete_constraint_outputport\
    import DeleteConstraintOutputPort


@dataclass
class DeleteConstraintOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: DeleteConstraintOutputPort
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
        DeleteConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = DeleteConstraintOutputPort()
        return self

    def with_deleted(self, deleted: bool):
        """ This function fill the deleted in the contract

        Parameters:
        -----------
        deleted: bool
            the deleted of the DeleteConstraint

        Returns:
        --------
        DeleteConstraintOutputPortBuilder
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
        DeleteConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> DeleteConstraintOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        DeleteConstraintOutputPort
            the contract filled

        """

        return self.__output
