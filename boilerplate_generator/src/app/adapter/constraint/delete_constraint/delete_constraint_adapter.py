""" This module use the usecase DeleteConstraint"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.usecase_container\
    import UsecaseContainer
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.delete_constraint.delete_constraint_inputport_builder\
    import DeleteConstraintInputPortBuilder


class DeleteConstraintAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase DeleteConstraint.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into DeleteConstraintInputPort
        with the use of DeleteConstraintInputPortBuilder.
        Then this contract will be gave to DeleteConstraint usecase.
        In return we should obtain the contract DeleteConstraintOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the constraint
            project_name: str
                The name of the project

        Returns:
        --------
        DeleteConstraint_oc
            the output contract of the usecase DeleteConstraint

        """

        sanitize_name = inputs["name"]

        sanitize_project_name = inputs["project_name"]

        delete_constraint_icb = DeleteConstraintInputPortBuilder()
        delete_constraint_ic = delete_constraint_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_project_name(sanitize_project_name)\
            .build()

        delete_constraint_oc = UsecaseContainer\
            .get("DeleteConstraint", storage_engine)\
            .execute(delete_constraint_ic)

        return delete_constraint_oc
