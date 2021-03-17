"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.read_usecase.read_usecase_inputport\
    import ReadUsecaseInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.read_usecase.read_usecase_outputport_builder\
    import ReadUsecaseOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.read_usecase.read_usecase_outputport\
    import ReadUsecaseOutputPort


@dataclass
class ReadUsecase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ReadUsecaseOutputPort
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
        self.builder = ReadUsecaseOutputPortBuilder()

    def execute(self, inputp: ReadUsecaseInputPort) -> ReadUsecaseOutputPort:
        """This function will from the inputport create a Usecase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ReadUsecaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ReadUsecaseOutputPort:
            The output contract

        """

        executed = False
        usecase = None

        name = inputp.name
        project_name = inputp.project_name

        identifier = (name, project_name)

        usecase = self.gateway.find_by_identifier(identifier)

        if usecase is None:
            error = "This Usecase, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True

        if executed:
            self.__output = self.builder.create()\
                                .with_name(usecase.name)\
                                .with_description(usecase.description)\
                                .with_type_(usecase.type_)\
                                .with_entity_name(usecase.entity_name)\
                                .with_project_name(usecase.project_name)\
                                .with_input_attrs(usecase.input_attrs)\
                                .with_output_attrs(usecase.output_attrs)\
                                .build()

        elif not executed and usecase is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
