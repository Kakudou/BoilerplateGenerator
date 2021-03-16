"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.list_constraint.list_constraint_outputport\
    import ListConstraintOutputPort


@dataclass
class ListConstraintOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListConstraintOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_all_constraints: List[str]
        fill the all_constraints in the contract
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
        ListConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListConstraintOutputPort()
        return self

    def with_all_constraints(self, all_constraints: List[str]):
        """ This function fill the all_constraints in the contract

        Parameters:
        -----------
        all_constraints: List[str]
            the all_constraints of the ListConstraint

        Returns:
        --------
        ListConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.all_constraints = all_constraints
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ListConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListConstraintOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListConstraintOutputPort
            the contract filled

        """

        return self.__output
