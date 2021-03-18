""" This module use the usecase DeleteEntity"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.delete_entity.delete_entity_inputport_builder\
    import DeleteEntityInputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.delete_usecase.delete_usecase_inputport_builder\
    import DeleteUsecaseInputPortBuilder
from boilerplate_generator.src.boilerplate_generator.usecase.\
    usecase.list_usecase_by_ent.list_usecase_by_ent_inputport_builder\
    import ListUsecaseByEntInputPortBuilder


class DeleteEntityAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase DeleteEntity.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into DeleteEntityInputPort
        with the use of DeleteEntityInputPortBuilder.
        Then this contract will be gave to DeleteEntity usecase.
        In return we should obtain the contract DeleteEntityOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            project_name: str
                The name of the project
            name: str
                The name of the entity

        Returns:
        --------
        DeleteEntity_oc
            the output contract of the usecase DeleteEntity

        """

        sanitize_project_name = inputs["project_name"]

        sanitize_name = inputs["name"]

        delete_entity_icb = DeleteEntityInputPortBuilder()
        delete_entity_ic = delete_entity_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .with_name(sanitize_name)\
            .build()

        delete_entity_oc = UsecaseContainer\
            .get("DeleteEntity", storage_engine)\
            .execute(delete_entity_ic)

        list_usecase_icb = ListUsecaseByEntInputPortBuilder()
        list_usecase_ic = list_usecase_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .with_entity_name(sanitize_name)\
            .build()

        list_usecase_oc = UsecaseContainer\
            .get("ListUsecaseByEnt", storage_engine)\
            .execute(list_usecase_ic)

        for usecase_name in list_usecase_oc.all_usecases:

            delete_usecase_icb = DeleteUsecaseInputPortBuilder()
            delete_usecase_ic = delete_usecase_icb\
                .create()\
                .with_project_name(sanitize_project_name)\
                .with_name(usecase_name)\
                .build()

            UsecaseContainer\
                .get("DeleteUsecase", storage_engine)\
                .execute(delete_usecase_ic)

        return delete_entity_oc
