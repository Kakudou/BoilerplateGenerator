"""This module is the core defined entity for Entity"""
import re

from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class Entity:
    """This class defined the attributes for Entity

    Attributes:
    -----------
    __project_name: str
        The name of the project
    __name: str
        The name of the entity
    __snakename: str
          The snake case name of the project
    __domain: str
        The domain of the entity
    __snakedomain: str
          The snake case domain of the project
    __attributes: List
        The attributes owned by the entity

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __project_name: str = None
    __name: str = None
    __snakename: str = None
    __domain: str = None
    __snakedomain: str = None
    __attributes: List = None

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
        self.__snakename = re.sub(r'(?!^)([A-Z]+)', r'_\1', name).lower()

    @property
    def snakename(self) -> str:
        return self.__snakename

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

    @property
    def attributes(self) -> List:
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: List):
        self.__attributes = attributes
