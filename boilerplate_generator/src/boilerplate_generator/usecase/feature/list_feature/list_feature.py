"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.list_feature.list_feature_inputport\
    import ListFeatureInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.list_feature.list_feature_outputport_builder\
    import ListFeatureOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.list_feature.list_feature_outputport\
    import ListFeatureOutputPort


@dataclass
class ListFeature:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: ListFeatureOutputPort
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
        self.builder = ListFeatureOutputPortBuilder()

    def execute(self, inputp: ListFeatureInputPort) -> ListFeatureOutputPort:
        """This function will from the inputport create a Feature
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: ListFeatureInputPort
            the inputport who come from the adapter

        Returns:
        --------
        ListFeatureOutputPort:
            The output contract

        """

        executed = False
        feature = None

        project_name = inputp.project_name

        all_features = self.gateway.find_all_by_project(project_name)

        if all_features is None:
            error = "Nothing was found."
            self.__output = self.builder.create().with_error(error).build()
        else:
            executed = True
            feature = True

        if executed:
            self.__output = self.builder.create()\
                                .with_all_features(all_features)\
                                .build()
        elif not executed and feature is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
