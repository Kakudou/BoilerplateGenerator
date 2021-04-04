"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.delete_entity.delete_entity_inputport\
    import DeleteEntityInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.delete_entity.delete_entity_outputport_builder\
    import DeleteEntityOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.delete_entity.delete_entity_outputport\
    import DeleteEntityOutputPort


@dataclass
class DeleteEntity:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: DeleteEntityOutputPort
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
        self.builder = DeleteEntityOutputPortBuilder()

    def execute(self, inputp: DeleteEntityInputPort) -> DeleteEntityOutputPort:
        """This function will from the inputport create a Entity
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: DeleteEntityInputPort
            the inputport who come from the adapter

        Returns:
        --------
        DeleteEntityOutputPort:
            The output contract

        """

        executed = False
        entity = None

        project_name = inputp.project_name
        name = inputp.name

        identifier = (project_name, name)

        entity_deleted = self.gateway.destroy_by_identifier(identifier)

        if entity_deleted:
            error = "This Entity Entity, doesn't look like to exist in BoilerplateGenerator"
            self.__output = self.builder.create().with_error(error).build()
            executed = True
            entity = True

        if executed:
            self.__output = self.builder.create()\
                                .with_deleted(entity_deleted)\
                                .build()

        elif not executed and entity is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
