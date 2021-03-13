"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.create_project.create_project_inputport\
    import CreateProjectInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.create_project.create_project_outputport_builder\
    import CreateProjectOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.create_project.create_project_outputport\
    import CreateProjectOutputPort
from boilerplate_generator.src.boilerplate_generator.entity.\
    project.project\
    import Project


@dataclass
class CreateProject:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: CreateProjectOutputPort
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
        self.builder = CreateProjectOutputPortBuilder()

    def execute(self, inputp: CreateProjectInputPort) -> CreateProjectOutputPort:
        """This function will from the inputport create a Project
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: CreateProjectInputPort
            the inputport who come from the adapter

        Returns:
        --------
        CreateProjectOutputPort:
            The output contract

        """

        executed = False
        project = None

        name = inputp.name
        path = inputp.path
        types = inputp.types

        identifier = (name)

        project = self.gateway.exist_by_identifier(identifier)

        if project:
            error = "The Project you want, already exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            project = Project()
            project.name = name
            project.path = path
            project.types = types

            executed = self.gateway.save(project)

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
