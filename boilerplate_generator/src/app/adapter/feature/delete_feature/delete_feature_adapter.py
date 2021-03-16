""" This module use the usecase DeleteFeature"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.delete_feature.delete_feature_inputport_builder\
    import DeleteFeatureInputPortBuilder


class DeleteFeatureAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase DeleteFeature.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into DeleteFeatureInputPort
        with the use of DeleteFeatureInputPortBuilder.
        Then this contract will be gave to DeleteFeature usecase.
        In return we should obtain the contract DeleteFeatureOutputPort

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
        DeleteFeature_oc
            the output contract of the usecase DeleteFeature

        """

        sanitize_name = inputs["name"]

        sanitize_project_name = inputs["project_name"]

        delete_feature_icb = DeleteFeatureInputPortBuilder()
        delete_feature_ic = delete_feature_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_project_name(sanitize_project_name)\
            .build()

        delete_feature_oc = UsecaseContainer\
            .get("DeleteFeature", storage_engine)\
            .execute(delete_feature_ic)

        return delete_feature_oc
