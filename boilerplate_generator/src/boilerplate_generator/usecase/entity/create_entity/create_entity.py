"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.create_entity.create_entity_inputport\
    import CreateEntityInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.create_entity.create_entity_outputport_builder\
    import CreateEntityOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.create_entity.create_entity_outputport\
    import CreateEntityOutputPort
from boilerplate_generator.src.boilerplate_generator.entity.\
    entity.entity\
    import Entity


@dataclass
class CreateEntity:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: CreateEntityOutputPort
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
        self.builder = CreateEntityOutputPortBuilder()

    def execute(self, inputp: CreateEntityInputPort) -> CreateEntityOutputPort:
        """This function will from the inputport create a Entity
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: CreateEntityInputPort
            the inputport who come from the adapter

        Returns:
        --------
        CreateEntityOutputPort:
            The output contract

        """

        executed = False
        entity = None

        project_name = inputp.project_name
        name = inputp.name
        domain = inputp.domain
        attributes = inputp.attributes

        identifier = (project_name, name)

        entity = self.gateway.exist_by_identifier(identifier)

        if entity:
            error = "The Entity you want, already exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            entity = Entity()
            entity.project_name = project_name
            entity.name = name
            entity.domain = domain
            entity.attributes = attributes

            executed = self.gateway.save(entity)

        if executed:
            self.__output = self.builder.create()\
                                .with_project_name(entity.project_name)\
                                .with_name(entity.name)\
                                .with_domain(entity.domain)\
                                .with_attributes(entity.attributes)\
                                .build()

        elif not executed and entity is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
