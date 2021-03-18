"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.generate_constraint.generate_constraint_inputport\
    import GenerateConstraintInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.generate_constraint.generate_constraint_outputport_builder\
    import GenerateConstraintOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.generate_constraint.generate_constraint_outputport\
    import GenerateConstraintOutputPort


@dataclass
class GenerateConstraint:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: GenerateConstraintOutputPort
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
        self.builder = GenerateConstraintOutputPortBuilder()

    def execute(self, inputp: GenerateConstraintInputPort) -> GenerateConstraintOutputPort:
        """This function will from the inputport create a Constraint
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: GenerateConstraintInputPort
            the inputport who come from the adapter

        Returns:
        --------
        GenerateConstraintOutputPort:
            The output contract

        """

        executed = False
        constraint = None

        constraint_name = inputp.constraint_name
        force = inputp.force
        project_name = inputp.project_name
        project_path = inputp.project_path
        project_types = inputp.project_types

        identifier = (constraint_name, project_name)

        # TODO: Implement your custom code
        raise NotImplementedError

        if executed:
            self.__output = self.builder.create()\
                                .with_folders(constraint.folders)\
                                .with_files(constraint.files)\
                                .build()

        elif not executed and constraint is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
