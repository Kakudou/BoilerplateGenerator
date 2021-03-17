"""This module is the EntityDTO that will be persist"""
from dataclasses\
    import dataclass
from typing\
    import List, Dict


@dataclass
class EntityDTO:
    """This class defined the attributes that we want to be persist

    Attributes:
    -----------
    __id: str
        The hash of the identifier of Entity: (project_name, name)
    __project_name: str
        The name of the project
    __name: str
        The name of the entity
    __domain: str
        The domain of the entity
    __attributes: List
        The attributes owned by the entity

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __id: str = None
    __project_name: str = None
    __name: str = None
    __domain: str = None
    __attributes: List = None

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def project_name(self) -> str:
        return self.__project_name

    @project_name.setter
    def project_name(self, project_name: str):
        self.__project_name = project_name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def attributes(self) -> List:
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: List):
        self.__attributes = attributes

    def to_yaml(self) -> Dict[str, str]:
        obj_to_yaml = {
            "name": self.name,
            "domain": self.domain,
        }
        if len(self.attributes) > 0:
            obj_to_yaml["attributes"] = self.attributes

        return obj_to_yaml

    def from_yaml(self, yaml):
        self.name = yaml["name"]
        self.domain = yaml["domain"]
        self.attributes = yaml["attributes"]\
            if "attributes" in yaml.keys() else {}
