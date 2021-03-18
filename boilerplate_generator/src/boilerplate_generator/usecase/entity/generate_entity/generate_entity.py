"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.generate_entity.generate_entity_inputport\
    import GenerateEntityInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.generate_entity.generate_entity_outputport_builder\
    import GenerateEntityOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.generate_entity.generate_entity_outputport\
    import GenerateEntityOutputPort


@dataclass
class GenerateEntity:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: GenerateEntityOutputPort
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
        self.builder = GenerateEntityOutputPortBuilder()

    def execute(self, inputp: GenerateEntityInputPort) -> GenerateEntityOutputPort:
        """This function will from the inputport create a Entity
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: GenerateEntityInputPort
            the inputport who come from the adapter

        Returns:
        --------
        GenerateEntityOutputPort:
            The output contract

        """

        executed = False
        entity = None

        entity_name = inputp.entity_name
        force = inputp.force
        project_name = inputp.project_name
        project_path = inputp.project_path
        project_types = inputp.project_types

        identifier = (entity_name, project_name)

        # TODO: Implement your custom code
        raise NotImplementedError

        if executed:
            self.__output = self.builder.create()\
                                .with_folders(entity.folders)\
                                .with_files(entity.files)\
                                .build()

        elif not executed and entity is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
