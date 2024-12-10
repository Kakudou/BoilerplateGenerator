""" This module use the usecase UpdateConstraint"""
from typing\
    import Dict

from boilerplate_generator.src\
    import STORAGE_ENGINE

from boilerplate_generator.src.utils.container\
    import Container
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.update_constraint.update_constraint_inputport_builder\
    import UpdateConstraintInputPortBuilder


class UpdateConstraintAdapter:
    """This class gonna take the input, sanitize and give it to the usecase.

    Functions:
    ----------
    execute: staticmethod
        will consume the usecase UpdateConstraint.

    """

    @staticmethod
    def execute(inputs: Dict, storage_engine=STORAGE_ENGINE):
        """This function will convert inputs into UpdateConstraintInputPort
        with the use of UpdateConstraintInputPortBuilder.
        Then this contract will be gave to UpdateConstraint usecase.
        In return we should obtain the contract UpdateConstraintOutputPort

        Parameters:
        -----------
        inputs: Dict
            a Dict containing the inputs:
            name: str
                The name of the constraint
            project_name: str
                The name of the project
            type_: str
                The type_ of the constraint
            domain: str
                The domain of the constraint
            description: str
                The description of the constraint
            scenario: str
                The description of the scenario
            given: str
                The given of the scenario
            when: str
                The when of the scenario
            then: str
                The then of the scenario

        Returns:
        --------
        UpdateConstraint_oc
            the output contract of the usecase UpdateConstraint

        """

        sanitize_name = inputs["name"]
        sanitize_project_name = inputs["project_name"]
        sanitize_type_ = inputs["type_"]
        sanitize_domain = inputs["domain"]
        sanitize_description = inputs["description"]
        sanitize_scenario = inputs["scenario"]
        sanitize_given = inputs["given"]
        sanitize_when = inputs["when"]
        sanitize_then = inputs["then"]

        update_constraint_icb = UpdateConstraintInputPortBuilder()
        update_constraint_ic = update_constraint_icb\
            .create()\
            .with_name(sanitize_name)\
            .with_project_name(sanitize_project_name)\
            .with_type_(sanitize_type_)\
            .with_domain(sanitize_domain)\
            .with_description(sanitize_description)\
            .with_scenario(sanitize_scenario)\
            .with_given(sanitize_given)\
            .with_when(sanitize_when)\
            .with_then(sanitize_then)\
            .build()

        update_constraint_oc = Container\
            .get_usecase_repo("UpdateConstraint", storage_engine)\
            .execute(update_constraint_ic)

        return update_constraint_oc
