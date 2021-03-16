""" This module use the usecase UpdateEntity"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.update_entity.update_entity_inputport_builder\
    import UpdateEntityInputPortBuilder


class UpdateEntityAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase UpdateEntity.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into UpdateEntityInputPort
        with the use of UpdateEntityInputPortBuilder.
        Then this contract will be gave to UpdateEntity usecase.
        In return we should obtain the contract UpdateEntityOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            project_name: str
                The name of the project
            name: str
                The name of the entity
            domain: str
                The domain of the entity
            attributes: List
                The attributes owned by the entity

        Returns:
        --------
        UpdateEntity_oc
            the output contract of the usecase UpdateEntity

        """

        sanitize_project_name = inputs["project_name"]

        sanitize_name = inputs["name"]

        sanitize_domain = inputs["domain"]

        sanitize_attributes = inputs["attributes"]

        update_entity_icb = UpdateEntityInputPortBuilder()
        update_entity_ic = update_entity_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .with_name(sanitize_name)\
            .with_domain(sanitize_domain)\
            .with_attributes(sanitize_attributes)\
            .build()

        update_entity_oc = UsecaseContainer\
            .get("UpdateEntity", storage_engine)\
            .execute(update_entity_ic)

        return update_entity_oc
