"""This module is the core defined entity for Project"""
import re

from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class Project:
    """This class defined the attributes for Project

    Attributes:
    -----------
    __name: str
        The name of the project
    __snakename: str
          The snake case name of the project
    __path: str
        The path of the project
    __types: List[str]
        The type of the project

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __name: str = None
    __snakename: str = None
    __path: str = None
    __types: List[str] = None

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
