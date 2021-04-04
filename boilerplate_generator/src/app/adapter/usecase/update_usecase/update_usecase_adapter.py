""" This module use the usecase UpdateUsecase"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.update_usecase.update_usecase_inputport_builder\
    import UpdateUsecaseInputPortBuilder


class UpdateUsecaseAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase UpdateUsecase.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into UpdateUsecaseInputPort
        with the use of UpdateUsecaseInputPortBuilder.
        Then this contract will be gave to UpdateUsecase usecase.
        In return we should obtain the contract UpdateUsecaseOutputPort

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
        UpdateUsecase_oc
            the output contract of the usecase UpdateUsecase

        """

        sanitize_project_name = inputs["project_name"]
        sanitize_entity_name = inputs["entity_name"]
        sanitize_type_ = inputs["type_"]
        sanitize_name = inputs["name"]
        sanitize_description = inputs["description"]
        sanitize_input_attrs = inputs["input_attrs"]
        sanitize_output_attrs = inputs["output_attrs"]

        update_usecase_icb = UpdateUsecaseInputPortBuilder()
        update_usecase_ic = update_usecase_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_description(sanitize_description)\
            .with_type_(sanitize_type_)\
            .with_entity_name(sanitize_entity_name)\
            .with_project_name(sanitize_project_name)\
            .with_input_attrs(sanitize_input_attrs)\
            .with_output_attrs(sanitize_output_attrs)\
            .build()

        update_usecase_oc = Container\
            .get_usecase("UpdateUsecase", storage_engine)\
            .execute(update_usecase_ic)

        return update_usecase_oc
