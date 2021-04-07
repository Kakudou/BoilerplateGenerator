""" This module use the usecase ListEntity"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.list_entity.list_entity_inputport_builder\
    import ListEntityInputPortBuilder


class ListEntityAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ListEntity.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ListEntityInputPort
        with the use of ListEntityInputPortBuilder.
        Then this contract will be gave to ListEntity usecase.
        In return we should obtain the contract ListEntityOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:

        Returns:
        --------
        ListEntity_oc
            the output contract of the usecase ListEntity

        """

        sanitize_project_name = inputs["project_name"]

        list_entity_icb = ListEntityInputPortBuilder()
        list_entity_ic = list_entity_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .build()

        list_entity_oc = Container\
            .get_usecase_repo("ListEntity", storage_engine)\
            .execute(list_entity_ic)

        return list_entity_oc
