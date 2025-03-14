"""This module is the FeatureDTO that will be persist"""
from dataclasses\
    import dataclass
from typing\
    import Dict


@dataclass
class FeatureDTO:
    """This class defined the attributes that we want to be persist

    Attributes:
    -----------
    __id: str
        The hash of the identifier of Feature: (name, project_name)
    __name: str
        The name of the feature
    __project_name: str
        The name of the project
    __type_: str
        The type_ of the feature
    __domain: str
        The domain of the feature
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

    __id: str = None
    __name: str = None
    __project_name: str = None
    __type_: str = None
    __domain: str = None
    __description: str = None
    __scenario: str = None
    __given: str = None
    __when: str = None
    __then: str = None

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def type_(self) -> str:
        return self.__type_

    @type_.setter
    def type_(self, type_: str):
        self.__type_ = type_

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

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

    def to_yaml(self) -> Dict[str, str]:
        obj_to_yaml = {
            "name": self.name,
            "type": self.type_,
            "domain": self.domain,
            "description": self.description,
            "scenario": self.scenario,
            "given": self.given,
            "when": self.when,
            "then": self.then,
        }

        return obj_to_yaml

    def from_yaml(self, yaml):
        self.name = yaml["name"]
        self.type_ = yaml["type"]
        self.domain = yaml["domain"]
        self.description = yaml["description"]
        self.scenario = yaml["scenario"]
        self.given = yaml["given"]
        self.when = yaml["when"]
        self.then = yaml["then"]
