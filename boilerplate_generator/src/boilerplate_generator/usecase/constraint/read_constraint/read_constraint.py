"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.read_constraint.read_constraint_inputport\
    import ReadConstraintInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.read_constraint.read_constraint_outputport_builder\
    import ReadConstraintOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.read_constraint.read_constraint_outputport\
    import ReadConstraintOutputPort


@dataclass
class ReadConstraint:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ReadConstraintOutputPort
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
        the container utils class give it the good implemented_gateway

        Parameters:
        -----------
        implemented_gateway:
            The implemented_gateway for the storage engine we want
        """

        self.gateway = implemented_gateway
        self.builder = ReadConstraintOutputPortBuilder()

    def execute(self, inputp: ReadConstraintInputPort) -> ReadConstraintOutputPort:
        """This function will from the inputport create a Constraint
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ReadConstraintInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ReadConstraintOutputPort:
            The output contract

        """

        executed = False
        constraint = None

        name = inputp.name
        project_name = inputp.project_name

        identifier = (name, project_name)

        constraint = self.gateway.find_by_identifier(identifier)

        if constraint is None:
            error = "This Constraint, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True

        if executed:
            self.__output = self.builder.create()\
                                .with_name(constraint.name)\
                                .with_project_name(constraint.project_name)\
                                .with_description(constraint.description)\
                                .with_scenario(constraint.scenario)\
                                .with_given(constraint.given)\
                                .with_when(constraint.when)\
                                .with_then(constraint.then)\
                                .build()

        elif not executed and constraint is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
