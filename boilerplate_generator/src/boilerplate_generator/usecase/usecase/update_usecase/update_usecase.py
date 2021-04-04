"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.update_usecase.update_usecase_inputport\
    import UpdateUsecaseInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.update_usecase.update_usecase_outputport_builder\
    import UpdateUsecaseOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.update_usecase.update_usecase_outputport\
    import UpdateUsecaseOutputPort


@dataclass
class UpdateUsecase:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: UpdateUsecaseOutputPort
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
        self.builder = UpdateUsecaseOutputPortBuilder()

    def execute(self, inputp: UpdateUsecaseInputPort) -> UpdateUsecaseOutputPort:
        """This function will from the inputport create a Usecase
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: UpdateUsecaseInputPort
            the inputport who come from the adapter

        Returns:
        --------
        UpdateUsecaseOutputPort:
            The output contract

        """

        executed = False
        usecase = None

        name = inputp.name
        description = inputp.description
        type_ = inputp.type_
        entity_name = inputp.entity_name
        project_name = inputp.project_name
        input_attrs = inputp.input_attrs
        output_attrs = inputp.output_attrs

        identifier = (name, project_name)

        usecase = self.gateway.find_by_identifier(identifier)

        if usecase is None:
            error = "The Usecase you want, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            usecase.name = name
            usecase.description = description
            usecase.type_ = type_
            usecase.entity_name = entity_name
            usecase.project_name = project_name
            usecase.input_attrs = input_attrs
            usecase.output_attrs = output_attrs

            executed = self.gateway.update_by_identifier(identifier, usecase)

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
