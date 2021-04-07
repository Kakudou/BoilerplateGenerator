""" This module use the usecase ListConstraint"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.list_constraint.list_constraint_inputport_builder\
    import ListConstraintInputPortBuilder


class ListConstraintAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase ListConstraint.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into ListConstraintInputPort
        with the use of ListConstraintInputPortBuilder.
        Then this contract will be gave to ListConstraint usecase.
        In return we should obtain the contract ListConstraintOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:

        Returns:
        --------
        ListConstraint_oc
            the output contract of the usecase ListConstraint

        """
        sanitize_project_name = inputs["project_name"]

        list_constraint_icb = ListConstraintInputPortBuilder()
        list_constraint_ic = list_constraint_icb\
            .create()\
            .with_project_name(sanitize_project_name)\
            .build()

        list_constraint_oc = Container\
            .get_usecase_repo("ListConstraint", storage_engine)\
            .execute(list_constraint_ic)

        return list_constraint_oc
