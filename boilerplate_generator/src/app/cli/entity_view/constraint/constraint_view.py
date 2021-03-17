"""This module is the Constraint that will be shown"""
from dataclasses\
    import dataclass


@dataclass
class ConstraintView:
    """This class defined the attributes that we want to show

    Attributes:
    -----------
    __name: str
        The name of the constraint
    __project_name: str
        The name of the project
    __description: str
        The description of the constraint
    __scenario: str
        The description of the scenario
    __given: str
        The given of the scenario
    __when: str
        The when of the scenario
    __then: str
        The then of the scenario

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __name: str = None
    __project_name: str = None
    __description: str = None
    __scenario: str = None
    __given: str = None
    __when: str = None
    __then: str = None

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def project_name(self) -> str:
        return self.__project_name

    @project_name.setter
    def project_name(self, project_name: str):
        self.__project_name = project_name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def scenario(self) -> str:
        return self.__scenario

    @scenario.setter
    def scenario(self, scenario: str):
        self.__scenario = scenario

    @property
    def given(self) -> str:
        return self.__given

    @given.setter
    def given(self, given: str):
        self.__given = given

    @property
    def when(self) -> str:
        return self.__when

    @when.setter
    def when(self, when: str):
        self.__when = when

    @property
    def then(self) -> str:
        return self.__then

    @then.setter
    def then(self, then: str):
        self.__then = then

    @staticmethod
    def from_contract(contract):
        constraint = ConstraintView()
        constraint.name = contract.name
        constraint.project_name = contract.project_name
        constraint.description = contract.description
        constraint.scenario = contract.scenario
        constraint.given = contract.given
        constraint.when = contract.when
        constraint.then = contract.then

        return constraint