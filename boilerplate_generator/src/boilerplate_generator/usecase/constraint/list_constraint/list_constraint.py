"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.list_constraint.list_constraint_inputport\
    import ListConstraintInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.list_constraint.list_constraint_outputport_builder\
    import ListConstraintOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.list_constraint.list_constraint_outputport\
    import ListConstraintOutputPort


@dataclass
class ListConstraint:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListConstraintOutputPort
        is the outputport information who gonna travel to the adapter

    Functions:
    ----------
    __init__:
        classical constructor
    execute:
        execute the usecase logic

    """

    __output: Any = None

    def __init__(self, implemented_gateway):
        """This function is the constructor particularity:
        the usecase_container utils class give it the good implemented_gateway

        Parameters:
        -----------
        implemented_gateway:
            The implemented_gateway for the storage engine we want
        """

        self.gateway = implemented_gateway
        self.builder = ListConstraintOutputPortBuilder()

    def execute(self, inputp: ListConstraintInputPort) -> ListConstraintOutputPort:
        """This function will from the inputport create a Constraint
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListConstraintInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListConstraintOutputPort:
            The output contract

        """

        executed = False
        constraint = None

        project_name = inputp.project_name

        all_constraints = self.gateway.find_all_by_project(project_name)

        if all_constraints is None:
            error = "Nothing was found."
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True
            constraint = True

        if executed:
            self.__output = self.builder.create()\
                                .with_all_constraints(all_constraints)\
                                .build()

        elif not executed and constraint is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
