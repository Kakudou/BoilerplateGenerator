""" This module use the usecase CreateUsecase"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.create_usecase.create_usecase_inputport_builder\
    import CreateUsecaseInputPortBuilder


class CreateUsecaseAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase CreateUsecase.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into CreateUsecaseInputPort
        with the use of CreateUsecaseInputPortBuilder.
        Then this contract will be gave to CreateUsecase usecase.
        In return we should obtain the contract CreateUsecaseOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the usecase
            description: str
                The description of the usecase
            type_: str
                The type of the usecase CRUDL or custom
            entity_name: str
                The name of the entity
            project_name: str
                The name of the project
            input_attrs: List
                Additional input attributes for the usecase
            output_attrs: List
                Additional output attribute for the usecase

        Returns:
        --------
        CreateUsecase_oc
            the output contract of the usecase CreateUsecase

        """

        sanitize_project_name = inputs["project_name"]
        sanitize_entity_name = inputs["entity_name"]
        sanitize_type_ = inputs["type_"]
        sanitize_name = inputs["name"]\
            if "Custom" == inputs["type_"] else None
        sanitize_description = inputs["description"]\
            if "Custom" == inputs["type_"] else None
        sanitize_input_attrs = inputs["input_attrs"]\
            if "input_attrs" in inputs.keys() else None
        sanitize_output_attrs = inputs["output_attrs"]\
            if "output_attrs" in inputs.keys() else None

        create_usecase_icb = CreateUsecaseInputPortBuilder()
        create_usecase_ic = create_usecase_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_description(sanitize_description)\
            .with_type_(sanitize_type_)\
            .with_entity_name(sanitize_entity_name)\
            .with_project_name(sanitize_project_name)\
            .with_input_attrs(sanitize_input_attrs)\
            .with_output_attrs(sanitize_output_attrs)\
            .build()

        create_usecase_oc = UsecaseContainer\
            .get("CreateUsecase", storage_engine)\
            .execute(create_usecase_ic)

        return create_usecase_oc
