"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.list_constraint.list_constraint_inputport\
    import ListConstraintInputPort


@dataclass
class ListConstraintInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListConstraintInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
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
        ListConstraintInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListConstraintInputPort()
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the ListConstraint

        Returns:
        --------
        ListConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def build(self) -> ListConstraintInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListConstraintInputPort
            the contract filled

        """

        return self.__input
