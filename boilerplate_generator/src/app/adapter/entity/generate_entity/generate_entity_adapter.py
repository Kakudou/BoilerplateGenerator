""" This module use the usecase GenerateEntity"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.generate_entity.generate_entity_inputport_builder\
    import GenerateEntityInputPortBuilder


class GenerateEntityAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase GenerateEntity.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into GenerateEntityInputPort
        with the use of GenerateEntityInputPortBuilder.
        Then this contract will be gave to GenerateEntity usecase.
        In return we should obtain the contract GenerateEntityOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            entity_name: str
                The name of the entity
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
        GenerateEntity_oc
            the output contract of the usecase GenerateEntity

        """

        sanitize_entity_name = inputs["entity_name"]
        sanitize_force = inputs["force"]
        sanitize_project_name = inputs["project_name"]
        sanitize_project_path = inputs["project_path"]
        sanitize_project_types = inputs["project_types"]

        generate_entity_icb = GenerateEntityInputPortBuilder()
        generate_entity_ic = generate_entity_icb\
            .create()\
            .with_entity_name(sanitize_entity_name)\
            .with_force(sanitize_force)\
            .with_project_name(sanitize_project_name)\
            .with_project_path(sanitize_project_path)\
            .with_project_types(sanitize_project_types)\
            .build()

        generate_entity_oc = Container\
            .get_usecase("GenerateEntity", storage_engine)\
            .execute(generate_entity_ic)

        return generate_entity_oc
