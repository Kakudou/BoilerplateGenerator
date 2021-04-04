"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.update_constraint.update_constraint_inputport\
    import UpdateConstraintInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.update_constraint.update_constraint_outputport_builder\
    import UpdateConstraintOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.update_constraint.update_constraint_outputport\
    import UpdateConstraintOutputPort


@dataclass
class UpdateConstraint:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: UpdateConstraintOutputPort
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
        self.builder = UpdateConstraintOutputPortBuilder()

    def execute(self, inputp: UpdateConstraintInputPort) -> UpdateConstraintOutputPort:
        """This function will from the inputport create a Constraint
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: UpdateConstraintInputPort
            the inputport who come from the adapter

        Returns:
        --------
        UpdateConstraintOutputPort:
            The output contract

        """

        executed = False
        constraint = None

        name = inputp.name
        project_name = inputp.project_name
        description = inputp.description
        scenario = inputp.scenario
        given = inputp.given
        when = inputp.when
        then = inputp.then

        identifier = (name, project_name)

        constraint = self.gateway.find_by_identifier(identifier)

        if constraint is None:
            error = "The Constraint you want, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            constraint.name = name
            constraint.project_name = project_name
            constraint.description = description
            constraint.scenario = scenario
            constraint.given = given
            constraint.when = when
            constraint.then = then

            executed = self.gateway.update_by_identifier(identifier, constraint)

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
