"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    constraint.update_constraint.update_constraint_inputport\
    import UpdateConstraintInputPort


@dataclass
class UpdateConstraintInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: UpdateConstraintInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_name: str
        fill the name in the contract
    with_project_name: str
        fill the project_name in the contract
    with_type_: str
        fill the type_ in the contract
    with_domain: str
        fill the domain in the contract
    with_description: str
        fill the description in the contract
    with_scenario: str
        fill the scenario in the contract
    with_given: str
        fill the given in the contract
    with_when: str
        fill the when in the contract
    with_then: str
        fill the then in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        UpdateConstraintInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = UpdateConstraintInputPort()
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.name = name
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def with_type_(self, type_: str):
        """ This function fill the type_ in the contract

        Parameters:
        -----------
        type_: str
            the type_ of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.type_ = type_
        return self

    def with_domain(self, domain: str):
        """ This function fill the domain in the contract

        Parameters:
        -----------
        domain: str
            the domain of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.domain = domain
        return self

    def with_description(self, description: str):
        """ This function fill the description in the contract

        Parameters:
        -----------
        description: str
            the description of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.description = description
        return self

    def with_scenario(self, scenario: str):
        """ This function fill the scenario in the contract

        Parameters:
        -----------
        scenario: str
            the scenario of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.scenario = scenario
        return self

    def with_given(self, given: str):
        """ This function fill the given in the contract

        Parameters:
        -----------
        given: str
            the given of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.given = given
        return self

    def with_when(self, when: str):
        """ This function fill the when in the contract

        Parameters:
        -----------
        when: str
            the when of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.when = when
        return self

    def with_then(self, then: str):
        """ This function fill the then in the contract

        Parameters:
        -----------
        then: str
            the then of the UpdateConstraint

        Returns:
        --------
        UpdateConstraintOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.then = then
        return self

    def build(self) -> UpdateConstraintInputPort:
        """ This function return the filled contract

        Returns:
        --------
        UpdateConstraintInputPort
            the contract filled

        """

        return self.__input
