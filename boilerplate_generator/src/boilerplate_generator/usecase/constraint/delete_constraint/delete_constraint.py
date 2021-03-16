"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.delete_constraint.delete_constraint_inputport\
    import DeleteConstraintInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.delete_constraint.delete_constraint_outputport_builder\
    import DeleteConstraintOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.delete_constraint.delete_constraint_outputport\
    import DeleteConstraintOutputPort


@dataclass
class DeleteConstraint:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: DeleteConstraintOutputPort
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
        self.builder = DeleteConstraintOutputPortBuilder()

    def execute(self, inputp: DeleteConstraintInputPort) -> DeleteConstraintOutputPort:
        """This function will from the inputport create a Constraint
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: DeleteConstraintInputPort
            the inputport who come from the adapter

        Returns:
        --------
        DeleteConstraintOutputPort:
            The output contract

        """

        executed = False
        constraint = None

        name = inputp.name
        project_name = inputp.project_name

        identifier = (name, project_name)

        constraint_deleted = self.gateway.destroy_by_identifier(identifier)

        if constraint_deleted:
            error = "This Entity Constraint, doesn't look like to exist in BoilerplateGenerator"
            self.__output = self.builder.create().with_error(error).build()
            executed = True
            constraint = True

        if executed:
            self.__output = self.builder.create()\
                                .with_deleted(constraint_deleted)\
                                .build()

        elif not executed and constraint is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
