"""This module is the core logic to create a Entity"""
from dataclasses\
    import dataclass
from typing\
    import Any

from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.delete_feature.delete_feature_inputport\
    import DeleteFeatureInputPort
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.delete_feature.delete_feature_outputport_builder\
    import DeleteFeatureOutputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.delete_feature.delete_feature_outputport\
    import DeleteFeatureOutputPort


@dataclass
class DeleteFeature:
    """This class is the usecase to create a Entity

    Attributes:
    -----------
    __output: DeleteFeatureOutputPort
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
        self.builder = DeleteFeatureOutputPortBuilder()

    def execute(self, inputp: DeleteFeatureInputPort) -> DeleteFeatureOutputPort:
        """This function will from the inputport create a Feature
        and save it if none with the same identifier is found.
        And then return the appropriate outputport.

        Parameters:
        -----------
        inputport: DeleteFeatureInputPort
            the inputport who come from the adapter

        Returns:
        --------
        DeleteFeatureOutputPort:
            The output contract

        """

        executed = False
        feature = None

        name = inputp.name
        project_name = inputp.project_name

        identifier = (name, project_name)

        feature_deleted = self.gateway.destroy_by_identifier(identifier)

        if feature_deleted:
            error = "This Entity Feature, doesn't look like to exist in BoilerplateGenerator"
            self.__output = self.builder.create().with_error(error).build()
            executed = True
            feature = True

        if executed:
            self.__output = self.builder.create()\
                                .with_deleted(feature_deleted)\
                                .build()

        elif not executed and feature is None:
            error = "An error occured during persistence"
            self.__output = self.builder.create().with_error(error).build()

        return self.__output
