""" This module use the usecase GenerateStructureProject"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.generate_structure_project.generate_structure_project_inputport_builder\
    import GenerateStructureProjectInputPortBuilder


class GenerateStructureProjectAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: classmethod
        will consume the usecase GenerateStructureProject.

    """

    @classmethod
    def execute(cls, inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into GenerateStructureProjectInputPort
        with the use of GenerateStructureProjectInputPortBuilder.
        Then this contract will be gave to GenerateStructureProject usecase.
        In return we should obtain the contract GenerateStructureProjectOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            project_name: str
                The name of the project
            force: bool
                Force the generation

        Returns:
        --------
        GenerateStructureProject_oc
            the output contract of the usecase GenerateStructureProject

        """

        sanitize_project_name = inputs["project_name"]

        sanitize_force = inputs["force"]

        generate_structure_project_icb = GenerateStructureProjectInputPortBuilder()
        generate_structure_project_ic = generate_structure_project_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .with_force(sanitize_force)\
            .build()

        generate_structure_project_oc = UsecaseContainer\
            .get("GenerateStructureProject", storage_engine)\
            .execute(generate_structure_project_ic)

        return generate_structure_project_oc
