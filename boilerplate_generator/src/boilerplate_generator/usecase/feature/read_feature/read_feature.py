"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.read_feature.read_feature_inputport\
    import ReadFeatureInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.read_feature.read_feature_outputport_builder\
    import ReadFeatureOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.read_feature.read_feature_outputport\
    import ReadFeatureOutputPort


@dataclass
class ReadFeature:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ReadFeatureOutputPort
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
        self.builder = ReadFeatureOutputPortBuilder()

    def execute(self, inputp: ReadFeatureInputPort) -> ReadFeatureOutputPort:
        """This function will from the inputport create a Feature
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ReadFeatureInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ReadFeatureOutputPort:
            The output contract

        """

        executed = False
        feature = None

        name = inputp.name
        project_name = inputp.project_name

        identifier = (name, project_name)

        feature = self.gateway.find_by_identifier(identifier)

        if feature is None:
            error = "This Feature, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True

        if executed:
            self.__output = self.builder.create()\
                                .with_name(feature.name)\
                                .with_project_name(feature.project_name)\
                                .with_description(feature.description)\
                                .with_scenario(feature.scenario)\
                                .with_given(feature.given)\
                                .with_when(feature.when)\
                                .with_then(feature.then)\
                                .build()

        elif not executed and feature is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
