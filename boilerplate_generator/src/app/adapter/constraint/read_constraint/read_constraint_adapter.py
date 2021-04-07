""" This module use the usecase ReadConstraint"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.read_constraint.read_constraint_inputport_builder\
    import ReadConstraintInputPortBuilder


class ReadConstraintAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ReadConstraint.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ReadConstraintInputPort
        with the use of ReadConstraintInputPortBuilder.
        Then this contract will be gave to ReadConstraint usecase.
        In return we should obtain the contract ReadConstraintOutputPort

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
        ReadConstraint_oc
            the output contract of the usecase ReadConstraint

        """

        sanitize_name = inputs["name"]
        sanitize_project_name = inputs["project_name"]

        read_constraint_icb = ReadConstraintInputPortBuilder()
        read_constraint_ic = read_constraint_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_project_name(sanitize_project_name)\
            .build()

        read_constraint_oc = Container\
            .get_usecase_repo("ReadConstraint", storage_engine)\
            .execute(read_constraint_ic)

        return read_constraint_oc
