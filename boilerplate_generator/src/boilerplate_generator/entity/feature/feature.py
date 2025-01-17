"""This module is the core de fined entity for Feature"""
import re

from dataclasses\
    import dataclass


@dataclass
class Feature:
    """This class defined the attributes for Feature

    Attributes:
    -----------
    __name: str
        The name of the feature
    __snakename: str
        The snakename of the feature
    __project_name: str
        The name of the project
    __type: str
        The type of feature based on the project type
    __domain: str
        The domain of the entity
    __snakedomain: str
          The snake case domain of the project
    __description: str
        The description of the feature
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
    __domain: str = None
    __snakedomain: str = None
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

    @property
    def type_(self) -> str:
        return self.__type

    @type_.setter
    def type_(self, type_: str):
        self.__type = type_
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain
        self.__snakedomain = re.sub(r'(?!^)([A-Z]+)', r'_\1', domain).lower()

    @property
    def snakedomain(self) -> str:
        return self.__snakedomain

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
