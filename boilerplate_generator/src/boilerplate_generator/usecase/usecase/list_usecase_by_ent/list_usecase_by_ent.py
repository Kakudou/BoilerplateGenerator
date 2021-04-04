"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase_by_ent.list_usecase_by_ent_inputport\
    import ListUsecaseByEntInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase_by_ent.list_usecase_by_ent_outputport_builder\
    import ListUsecaseByEntOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase_by_ent.list_usecase_by_ent_outputport\
    import ListUsecaseByEntOutputPort


@dataclass
class ListUsecaseByEnt:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListUsecaseByEntOutputPort
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
        self.builder = ListUsecaseByEntOutputPortBuilder()

    def execute(self, inputp: ListUsecaseByEntInputPort) -> ListUsecaseByEntOutputPort:
        """This function will from the inputport create a Usecase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListUsecaseByEntInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListUsecaseByEntOutputPort:
            The output contract

        """

        executed = False
        usecase = None

        project_name = inputp.project_name
        entity_name = inputp.entity_name

        all_usecases = self.gateway.find_all_by_entity(project_name, entity_name)

        if all_usecases is None:
            error = "Nothing was found."
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True
            usecase = True

        if executed:
            self.__output = self.builder.create()\
                                .with_all_usecases(all_usecases)\
                                .build()

        elif not executed and usecase is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
