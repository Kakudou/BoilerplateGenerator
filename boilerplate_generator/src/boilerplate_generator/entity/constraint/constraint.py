"""This module is the core defined entity for Constraint"""
import re

from dataclasses\
    import dataclass


@dataclass
class Constraint:
    """This class defined the attributes for Constraint

    Attributes:
    -----------
    __name: str
        The name of the constraint
    __snakename: str
        The snakename of the constraint
    __project_name: str
        The name of the project
    __type: str
        The type of the constraint
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
    __snakename: str = None
    __project_name: str = None
    __type: str = None
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
        self.__snakename = re.sub(r'(?!^)([A-Z]+)', r'_\1', name).lower()

    @property
    def snakename(self) -> str:
        return self.__snakename

    @property
    def project_name(self) -> str:
        return self.__project_name

    @project_name.setter
    def project_name(self, project_name: str):
        self.__project_name = project_name

    @property
    def type_(self) -> str:
        return self.__type

    @type_.setter
    def type_(self, type_: str):
        self.__type = type_

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
