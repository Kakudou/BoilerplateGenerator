"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.delete_usecase.delete_usecase_inputport\
    import DeleteUsecaseInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.delete_usecase.delete_usecase_outputport_builder\
    import DeleteUsecaseOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.delete_usecase.delete_usecase_outputport\
    import DeleteUsecaseOutputPort


@dataclass
class DeleteUsecase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: DeleteUsecaseOutputPort
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
        self.builder = DeleteUsecaseOutputPortBuilder()

    def execute(self, inputp: DeleteUsecaseInputPort) -> DeleteUsecaseOutputPort:
        """This function will from the inputport create a Usecase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: DeleteUsecaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        DeleteUsecaseOutputPort:
            The output contract

        """

        executed = False
        usecase = None

        name = inputp.name
        project_name = inputp.project_name

        identifier = (name, project_name)

        usecase_deleted = self.gateway.destroy_by_identifier(identifier)

        if usecase_deleted:
            error = "This Entity Usecase, doesn't look like to exist in BoilerplateGenerator"
            self.__output = self.builder.create().with_error(error).build()
            executed = True
            usecase = True

        if executed:
            self.__output = self.builder.create()\
                                .with_deleted(usecase_deleted)\
                                .build()

        elif not executed and usecase is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
