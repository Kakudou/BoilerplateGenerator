""" This module use the usecase ReadFeature"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.read_feature.read_feature_inputport_builder\
    import ReadFeatureInputPortBuilder


class ReadFeatureAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ReadFeature.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ReadFeatureInputPort
        with the use of ReadFeatureInputPortBuilder.
        Then this contract will be gave to ReadFeature usecase.
        In return we should obtain the contract ReadFeatureOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the feature
            project_name: str
                The name of the project

        Returns:
        --------
        ReadFeature_oc
            the output contract of the usecase ReadFeature

        """

        sanitize_name = inputs["name"]

        sanitize_project_name = inputs["project_name"]

        read_feature_icb = ReadFeatureInputPortBuilder()
        read_feature_ic = read_feature_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_project_name(sanitize_project_name)\
            .build()

        read_feature_oc = UsecaseContainer\
            .get("ReadFeature", storage_engine)\
            .execute(read_feature_ic)

        return read_feature_oc
