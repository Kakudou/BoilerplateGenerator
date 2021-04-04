"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.create_usecase.create_usecase_inputport\
    import CreateUsecaseInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.create_usecase.create_usecase_outputport_builder\
    import CreateUsecaseOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.create_usecase.create_usecase_outputport\
    import CreateUsecaseOutputPort
from boilerplate_generator.src.boilerplate_generator.entity.\
    usecase.usecase\
    import Usecase


@dataclass
class CreateUsecase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: CreateUsecaseOutputPort
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
        self.builder = CreateUsecaseOutputPortBuilder()

    def execute(self, inputp: CreateUsecaseInputPort) -> CreateUsecaseOutputPort:
        """This function will from the inputport create a Usecase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: CreateUsecaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        CreateUsecaseOutputPort:
            The output contract

        """

        executed = False
        usecase = None

        project_name = inputp.project_name
        entity_name = inputp.entity_name
        type_ = inputp.type_

        name = inputp.name\
            if "Custom" == type_ else f"{type_}{entity_name}"
        description = inputp.description\
            if "Custom" == type_ else f"{type_} a {entity_name}"
        input_attrs = inputp.input_attrs
        output_attrs = inputp.output_attrs

        identifier = (name, project_name)

        usecase = self.gateway.exist_by_identifier(identifier)

        if usecase:
            error = "The Usecase you want, already exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            usecase = Usecase()
            usecase.project_name = project_name
            usecase.description = description
            usecase.entity_name = entity_name
            usecase.type_ = type_
            usecase.name = name
            usecase.input_attrs = input_attrs
            usecase.output_attrs = output_attrs

            executed = self.gateway.save(usecase)

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
