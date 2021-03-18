"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_inputport\
    import GenerateUsecaseInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_outputport_builder\
    import GenerateUsecaseOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_outputport\
    import GenerateUsecaseOutputPort


@dataclass
class GenerateUsecase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: GenerateUsecaseOutputPort
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
        self.builder = GenerateUsecaseOutputPortBuilder()

    def execute(self, inputp: GenerateUsecaseInputPort) -> GenerateUsecaseOutputPort:
        """This function will from the inputport create a Usecase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: GenerateUsecaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        GenerateUsecaseOutputPort:
            The output contract

        """

        executed = False
        usecase = None

        usecase_name = inputp.usecase_name
        entity_name = inputp.entity_name
        entity_domain = inputp.entity_domain
        entity_attributes = inputp.entity_attributes
        project_name = inputp.project_name
        project_path = inputp.project_path
        project_types = inputp.project_types

        identifier = (usecase_name, project_name)

        # TODO: Implement your custom code
        raise NotImplementedError

        if executed:
            self.__output = self.builder.create()\
                                .with_folders(usecase.folders)\
                                .with_files(usecase.files)\
                                .build()

        elif not executed and usecase is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
