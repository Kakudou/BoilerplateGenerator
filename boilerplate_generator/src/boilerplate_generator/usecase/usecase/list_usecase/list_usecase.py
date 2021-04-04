"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase.list_usecase_inputport\
    import ListUsecaseInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase.list_usecase_outputport_builder\
    import ListUsecaseOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase.list_usecase_outputport\
    import ListUsecaseOutputPort


@dataclass
class ListUsecase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListUsecaseOutputPort
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
        self.builder = ListUsecaseOutputPortBuilder()

    def execute(self, inputp: ListUsecaseInputPort) -> ListUsecaseOutputPort:
        """This function will from the inputport create a Usecase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListUsecaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListUsecaseOutputPort:
            The output contract

        """

        executed = False
        usecase = None

        project_name = inputp.project_name

        all_usecases = self.gateway.find_all_by_project(project_name)

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
