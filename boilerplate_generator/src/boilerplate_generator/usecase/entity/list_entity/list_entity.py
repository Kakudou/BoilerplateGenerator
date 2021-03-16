"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.list_entity.list_entity_inputport\
    import ListEntityInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.list_entity.list_entity_outputport_builder\
    import ListEntityOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.list_entity.list_entity_outputport\
    import ListEntityOutputPort


@dataclass
class ListEntity:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListEntityOutputPort
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
        self.builder = ListEntityOutputPortBuilder()

    def execute(self, inputp: ListEntityInputPort) -> ListEntityOutputPort:
        """This function will from the inputport create a Entity
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListEntityInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListEntityOutputPort:
            The output contract

        """

        executed = False
        entity = None

        project_name = inputp.project_name

        all_entitys = self.gateway.find_all_by_project(project_name)

        if all_entitys is None:
            error = "Nothing was found."
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True
            entity = True

        if executed:
            self.__output = self.builder.create()\
                                .with_all_entitys(all_entitys)\
                                .build()

        elif not executed and entity is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
