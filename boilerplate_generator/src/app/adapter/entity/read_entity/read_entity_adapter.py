""" This module use the usecase ReadEntity"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    entity.read_entity.read_entity_inputport_builder\
    import ReadEntityInputPortBuilder


class ReadEntityAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ReadEntity.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ReadEntityInputPort
        with the use of ReadEntityInputPortBuilder.
        Then this contract will be gave to ReadEntity usecase.
        In return we should obtain the contract ReadEntityOutputPort

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
        ReadEntity_oc
            the output contract of the usecase ReadEntity

        """

        sanitize_project_name = inputs["project_name"]
        sanitize_name = inputs["name"]

        read_entity_icb = ReadEntityInputPortBuilder()
        read_entity_ic = read_entity_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .with_name(sanitize_name)\
            .build()

        read_entity_oc = UsecaseContainer\
            .get("ReadEntity", storage_engine)\
            .execute(read_entity_ic)

        return read_entity_oc
