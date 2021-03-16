""" This module use the usecase CreateEntity"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.create_entity.create_entity_inputport_builder\
    import CreateEntityInputPortBuilder


class CreateEntityAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase CreateEntity.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into CreateEntityInputPort
        with the use of CreateEntityInputPortBuilder.
        Then this contract will be gave to CreateEntity usecase.
        In return we should obtain the contract CreateEntityOutputPort

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
        CreateEntity_oc
            the output contract of the usecase CreateEntity

        """

        sanitize_project_name = inputs["project_name"]

        sanitize_name = inputs["name"]

        sanitize_domain = inputs["domain"]

        sanitize_attributes = inputs["attributes"]

        create_entity_icb = CreateEntityInputPortBuilder()
        create_entity_ic = create_entity_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .with_name(sanitize_name)\
            .with_domain(sanitize_domain)\
            .with_attributes(sanitize_attributes)\
            .build()

        create_entity_oc = UsecaseContainer\
            .get("CreateEntity", storage_engine)\
            .execute(create_entity_ic)

        return create_entity_oc
