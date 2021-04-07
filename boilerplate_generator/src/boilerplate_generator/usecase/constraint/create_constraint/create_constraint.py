"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.create_constraint.create_constraint_inputport\
    import CreateConstraintInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.create_constraint.create_constraint_outputport_builder\
    import CreateConstraintOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.create_constraint.create_constraint_outputport\
    import CreateConstraintOutputPort
from boilerplate_generator.src.boilerplate_generator.entity.\
    constraint.constraint\
    import Constraint


@dataclass
class CreateConstraint:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: CreateConstraintOutputPort
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
        self.builder = CreateConstraintOutputPortBuilder()

    def execute(self, inputp: CreateConstraintInputPort) -> CreateConstraintOutputPort:
        """This function will from the inputport create a Constraint
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: CreateConstraintInputPort
            the inputport who come from the adapter

        Returns:
        --------
        CreateConstraintOutputPort:
            The output contract

        """

        executed = False
        constraint = None

        name = inputp.name
        project_name = inputp.project_name
        type_ = inputp.type_
        description = inputp.description
        scenario = inputp.scenario
        given = inputp.given
        when = inputp.when
        then = inputp.then

        identifier = (name, project_name)

        constraint = self.gateway.exist_by_identifier(identifier)

        if constraint:
            error = "The Constraint you want, already exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            constraint = Constraint()
            constraint.name = name
            constraint.project_name = project_name
            constraint.type_ = type_
            constraint.description = description
            constraint.scenario = scenario
            constraint.given = given
            constraint.when = when
            constraint.then = then

            executed = self.gateway.save(constraint)

        if executed:
            self.__output = self.builder.create()\
                                .with_name(constraint.name)\
                                .with_project_name(constraint.project_name)\
                                .with_type_(constraint.type_)\
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
