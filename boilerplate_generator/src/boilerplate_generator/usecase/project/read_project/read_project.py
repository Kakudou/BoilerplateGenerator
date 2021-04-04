"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.read_project.read_project_inputport\
    import ReadProjectInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.read_project.read_project_outputport_builder\
    import ReadProjectOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.read_project.read_project_outputport\
    import ReadProjectOutputPort


@dataclass
class ReadProject:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ReadProjectOutputPort
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
        self.builder = ReadProjectOutputPortBuilder()

    def execute(self, inputp: ReadProjectInputPort) -> ReadProjectOutputPort:
        """This function will from the inputport create a Project
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ReadProjectInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ReadProjectOutputPort:
            The output contract

        """

        executed = False
        project = None

        name = inputp.name

        identifier = (name)

        project = self.gateway.find_by_identifier(identifier)

        if project is None:
            error = "This Project, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True

        if executed:
            self.__output = self.builder.create()\
                                .with_name(project.name)\
                                .with_path(project.path)\
                                .with_types(project.types)\
                                .build()

        elif not executed and project is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
