""" This module use the usecase GenerateUsecase"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.generate_usecase.generate_usecase_inputport_builder\
    import GenerateUsecaseInputPortBuilder


class GenerateUsecaseAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase GenerateUsecase.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into GenerateUsecaseInputPort
        with the use of GenerateUsecaseInputPortBuilder.
        Then this contract will be gave to GenerateUsecase usecase.
        In return we should obtain the contract GenerateUsecaseOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            usecase_name: str
                The name of the usecase
            force: bool
                Force the generation
            entity_name: str
                The name of the entity
            entity_domain: str
                The domain of the entity
            entity_attributes: List[str]
                The attributes of the entity
            project_name: str
                The name of the project
            project_path: str
                The path of the project
            project_types: List[str]
                The type of the project

        Returns:
        --------
        GenerateUsecase_oc
            the output contract of the usecase GenerateUsecase

        """

        sanitize_usecase_name = inputs["usecase_name"]
        sanitize_force = inputs["force"]
        sanitize_entity_name = inputs["entity_name"]
        sanitize_entity_domain = inputs["entity_domain"]
        sanitize_entity_attributes = inputs["entity_attributes"]
        sanitize_project_name = inputs["project_name"]
        sanitize_project_path = inputs["project_path"]
        sanitize_project_types = inputs["project_types"]

        generate_usecase_icb = GenerateUsecaseInputPortBuilder()
        generate_usecase_ic = generate_usecase_icb\
            .create()\
            .with_usecase_name(sanitize_usecase_name)\
            .with_force(sanitize_force)\
            .with_entity_name(sanitize_entity_name)\
            .with_entity_domain(sanitize_entity_domain)\
            .with_entity_attributes(sanitize_entity_attributes)\
            .with_project_name(sanitize_project_name)\
            .with_project_path(sanitize_project_path)\
            .with_project_types(sanitize_project_types)\
            .build()

        generate_usecase_oc = Container\
            .get_usecase_repo("GenerateUsecase", storage_engine)\
            .execute(generate_usecase_ic)

        return generate_usecase_oc
