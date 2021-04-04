""" This module use the usecase GenerateConstraint"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.generate_constraint.generate_constraint_inputport_builder\
    import GenerateConstraintInputPortBuilder


class GenerateConstraintAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase GenerateConstraint.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into GenerateConstraintInputPort
        with the use of GenerateConstraintInputPortBuilder.
        Then this contract will be gave to GenerateConstraint usecase.
        In return we should obtain the contract GenerateConstraintOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            constraint_name: str
                The name of the constraint
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
        GenerateConstraint_oc
            the output contract of the usecase GenerateConstraint

        """

        sanitize_constraint_name = inputs["constraint_name"]
        sanitize_force = inputs["force"]
        sanitize_project_name = inputs["project_name"]
        sanitize_project_path = inputs["project_path"]
        sanitize_project_types = inputs["project_types"]

        generate_constraint_icb = GenerateConstraintInputPortBuilder()
        generate_constraint_ic = generate_constraint_icb\
            .create()\
            .with_constraint_name(sanitize_constraint_name)\
            .with_force(sanitize_force)\
            .with_project_name(sanitize_project_name)\
            .with_project_path(sanitize_project_path)\
            .with_project_types(sanitize_project_types)\
            .build()

        generate_constraint_oc = Container\
            .get_usecase("GenerateConstraint", storage_engine)\
            .execute(generate_constraint_ic)

        return generate_constraint_oc
