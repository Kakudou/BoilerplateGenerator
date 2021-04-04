"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.list_project.list_project_inputport\
    import ListProjectInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.list_project.list_project_outputport_builder\
    import ListProjectOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.list_project.list_project_outputport\
    import ListProjectOutputPort


@dataclass
class ListProject:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListProjectOutputPort
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
        self.builder = ListProjectOutputPortBuilder()

    def execute(self, inputp: ListProjectInputPort) -> ListProjectOutputPort:
        """This function will from the inputport create a Project
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListProjectInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListProjectOutputPort:
            The output contract

        """

        executed = False
        project = None

        all_projects = self.gateway.find_all()

        if all_projects is None:
            error = "Nothing was found."
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True
            project = True

        if executed:
            self.__output = self.builder.create()\
                                .with_all_projects(all_projects)\
                                .build()

        elif not executed and project is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
