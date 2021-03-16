"""This module is the Project that will be shown"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ProjectView:
    """This class defined the attributes that we want to show

    Attributes:
    -----------
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

    __name: str = None
    __path: str = None
    __types: List[str] = None

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

    @staticmethod
    def from_contract(contract):
        project = ProjectView()
        project.name = contract.name
        project.path = contract.path
        project.types = contract.types

        return project
