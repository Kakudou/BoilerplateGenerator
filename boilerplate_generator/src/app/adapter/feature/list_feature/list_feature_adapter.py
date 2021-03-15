""" This module use the usecase ListFeature"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.list_feature.list_feature_inputport_builder\
    import ListFeatureInputPortBuilder


class ListFeatureAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: classmethod
        will consume the usecase ListFeature.

    """

    @classmethod
    def execute(cls, inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ListFeatureInputPort
        with the use of ListFeatureInputPortBuilder.
        Then this contract will be gave to ListFeature usecase.
        In return we should obtain the contract ListFeatureOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:

        Returns:
        --------
        ListFeature_oc
            the output contract of the usecase ListFeature

        """
        sanitize_project_name = inputs["project_name"]

        list_feature_icb = ListFeatureInputPortBuilder()
        list_feature_ic = list_feature_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .build()

        list_feature_oc = UsecaseContainer\
            .get("ListFeature", storage_engine)\
            .execute(list_feature_ic)

        return list_feature_oc
