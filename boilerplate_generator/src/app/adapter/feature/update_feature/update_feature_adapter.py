""" This module use the usecase UpdateFeature"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.update_feature.update_feature_inputport_builder\
    import UpdateFeatureInputPortBuilder


class UpdateFeatureAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase UpdateFeature.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into UpdateFeatureInputPort
        with the use of UpdateFeatureInputPortBuilder.
        Then this contract will be gave to UpdateFeature usecase.
        In return we should obtain the contract UpdateFeatureOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the feature
            project_name: str
                The name of the project
            description: str
                The description of the feature
            scenario: str
                The description of the scenario
            given: str
                The given of the scenario
            when: str
                The when of the scenario
            then: str
                The then of the scenario

        Returns:
        --------
        UpdateFeature_oc
            the output contract of the usecase UpdateFeature

        """

        sanitize_name = inputs["name"]

        sanitize_project_name = inputs["project_name"]

        sanitize_description = inputs["description"]

        sanitize_scenario = inputs["scenario"]

        sanitize_given = inputs["given"]

        sanitize_when = inputs["when"]

        sanitize_then = inputs["then"]

        update_feature_icb = UpdateFeatureInputPortBuilder()
        update_feature_ic = update_feature_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_project_name(sanitize_project_name)\
            .with_description(sanitize_description)\
            .with_scenario(sanitize_scenario)\
            .with_given(sanitize_given)\
            .with_when(sanitize_when)\
            .with_then(sanitize_then)\
            .build()

        update_feature_oc = UsecaseContainer\
            .get("UpdateFeature", storage_engine)\
            .execute(update_feature_ic)

        return update_feature_oc
