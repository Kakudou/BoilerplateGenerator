""" This module use the usecase GenerateFeature"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.generate_feature.generate_feature_inputport_builder\
    import GenerateFeatureInputPortBuilder


class GenerateFeatureAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase GenerateFeature.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into GenerateFeatureInputPort
        with the use of GenerateFeatureInputPortBuilder.
        Then this contract will be gave to GenerateFeature usecase.
        In return we should obtain the contract GenerateFeatureOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            feature_name: str
                The name of the feature
            force: bool
                Force the generation
            project_name: str
                The name of the project
            project_path: str
                The path of the project
            project_types: List[str]
                The type of the project

        Returns:
        --------
        GenerateFeature_oc
            the output contract of the usecase GenerateFeature

        """

        sanitize_feature_name = inputs["feature_name"]
        sanitize_force = inputs["force"]
        sanitize_project_name = inputs["project_name"]
        sanitize_project_path = inputs["project_path"]
        sanitize_project_types = inputs["project_types"]

        generate_feature_icb = GenerateFeatureInputPortBuilder()
        generate_feature_ic = generate_feature_icb\
            .create()\
            .with_feature_name(sanitize_feature_name)\
            .with_force(sanitize_force)\
            .with_project_name(sanitize_project_name)\
            .with_project_path(sanitize_project_path)\
            .with_project_types(sanitize_project_types)\
            .build()

        generate_feature_oc = UsecaseContainer\
            .get("GenerateFeature", storage_engine)\
            .execute(generate_feature_ic)

        return generate_feature_oc
