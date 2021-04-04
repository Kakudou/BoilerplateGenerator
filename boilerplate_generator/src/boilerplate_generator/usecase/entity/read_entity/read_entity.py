"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.read_entity.read_entity_inputport\
    import ReadEntityInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.read_entity.read_entity_outputport_builder\
    import ReadEntityOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.read_entity.read_entity_outputport\
    import ReadEntityOutputPort


@dataclass
class ReadEntity:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ReadEntityOutputPort
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
        self.builder = ReadEntityOutputPortBuilder()

    def execute(self, inputp: ReadEntityInputPort) -> ReadEntityOutputPort:
        """This function will from the inputport create a Entity
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ReadEntityInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ReadEntityOutputPort:
            The output contract

        """

        executed = False
        entity = None

        project_name = inputp.project_name
        name = inputp.name

        identifier = (project_name, name)

        entity = self.gateway.find_by_identifier(identifier)

        if entity is None:
            error = "This Entity, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True

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
