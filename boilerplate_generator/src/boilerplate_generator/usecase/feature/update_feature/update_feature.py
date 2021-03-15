"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.update_feature.update_feature_inputport\
    import UpdateFeatureInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.update_feature.update_feature_outputport_builder\
    import UpdateFeatureOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.update_feature.update_feature_outputport\
    import UpdateFeatureOutputPort


@dataclass
class UpdateFeature:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: UpdateFeatureOutputPort
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
        self.builder = UpdateFeatureOutputPortBuilder()

    def execute(self, inputp: UpdateFeatureInputPort) -> UpdateFeatureOutputPort:
        """This function will from the inputport create a Feature
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: UpdateFeatureInputPort
            the inputport who come from the adapter

        Returns:
        --------
        UpdateFeatureOutputPort:
            The output contract

        """

        executed = False
        feature = None

        name = inputp.name
        project_name = inputp.project_name
        description = inputp.description
        scenario = inputp.scenario
        given = inputp.given
        when = inputp.when
        then = inputp.then

        identifier = (name, project_name)

        feature = self.gateway.find_by_identifier(identifier)

        if feature is None:
            error = "The Feature you want, doesn't look like to exist"
            self.__output = self.builder.create().with_error(error).build()
        else:
            feature.name = name
            feature.project_name = project_name
            feature.description = description
            feature.scenario = scenario
            feature.given = given
            feature.when = when
            feature.then = then

            executed = self.gateway.update_by_identifier(identifier, feature)

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
