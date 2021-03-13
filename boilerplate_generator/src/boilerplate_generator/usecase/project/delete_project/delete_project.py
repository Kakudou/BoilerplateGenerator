"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.delete_project.delete_project_inputport\
    import DeleteProjectInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.delete_project.delete_project_outputport_builder\
    import DeleteProjectOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.delete_project.delete_project_outputport\
    import DeleteProjectOutputPort


@dataclass
class DeleteProject:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: DeleteProjectOutputPort
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
        self.builder = DeleteProjectOutputPortBuilder()

    def execute(self, inputp: DeleteProjectInputPort) -> DeleteProjectOutputPort:
        """This function will from the inputport create a Project
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: DeleteProjectInputPort
            the inputport who come from the adapter

        Returns:
        --------
        DeleteProjectOutputPort:
            The output contract

        """

        executed = False
        project = None

        name = inputp.name

        identifier = (name)

        project_deleted = self.gateway.destroy_by_identifier(identifier)

        if project_deleted:
            error = "This Entity Project, doesn't look like to exist in BoilerplateGenerator"
            self.__output = self.builder.create().with_error(error).build()
            executed = True
            project = True

        if executed:
            self.__output = self.builder.create()\
                                .with_deleted(project_deleted)\
                                .build()

        elif not executed and project is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
