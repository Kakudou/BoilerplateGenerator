"""This module is the core defined entity for Entity"""
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
    __domain: str
        The domain of the entity
    __attributes: List
        The attributes owned by the entity

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __project_name: str = None
    __name: str = None
    __domain: str = None
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
