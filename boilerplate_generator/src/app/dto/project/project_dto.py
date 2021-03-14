"""This module is the ProjectDTO that will be persist"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ProjectDTO:
    """This class defined the attributes that we want to be persist

    Attributes:
    -----------
    __id: str
        The hash of the identifier of Project: (name)
    __name: str
        The name of the project
    __path: str
        The path of the project
    __types: List[str]
        The type of the project

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __id: str = None
    __name: str = None
    __path: str = None
    __types: List[str] = None

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
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def types(self) -> List[str]:
        return self.__types

    @types.setter
    def types(self, types: List[str]):
        self.__types = types

    def to_yaml(self) -> str:
        obj_to_yaml = {
            "project": {
                "name": self.name,
                "path": self.path,
                "types": self.types
            }
        }

        return obj_to_yaml

    def from_yaml(self, yaml):
        self.name = yaml["project"]["name"]
        self.path = yaml["project"]["path"]
        self.types = yaml["project"]["types"]
