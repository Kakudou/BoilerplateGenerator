"""This module is the core defined entity for Usecase"""
import re

from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class Usecase:
    """This class defined the attributes for Usecase

    Attributes:
    -----------
    __name: str
        The name of the usecase
    __snakename: str
          The snake case name of the project
    __description: str
        The description of the usecase
    __type_: str
        The type of the usecase CRUDL or custom
    __entity_name: str
        The name of the entity
    __project_name: str
        The name of the project
    __input_attrs: List
        Additional input attributes for the usecase
    __output_attrs: List
        Additional output attribute for the usecase

    Functions:
    ----------
    Getter and Setter for above attributes
    """

    __name: str = None
    __snakename: str = None
    __description: str = None
    __type_: str = None
    __entity_name: str = None
    __project_name: str = None
    __input_attrs: List = None
    __output_attrs: List = None

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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def type_(self) -> str:
        return self.__type_

    @type_.setter
    def type_(self, type_: str):
        self.__type_ = type_

    @property
    def entity_name(self) -> str:
        return self.__entity_name

    @entity_name.setter
    def entity_name(self, entity_name: str):
        self.__entity_name = entity_name

    @property
    def project_name(self) -> str:
        return self.__project_name

    @project_name.setter
    def project_name(self, project_name: str):
        self.__project_name = project_name

    @property
    def input_attrs(self) -> List:
        return self.__input_attrs

    @input_attrs.setter
    def input_attrs(self, input_attrs: List):
        self.__input_attrs = input_attrs

    @property
    def output_attrs(self) -> List:
        return self.__output_attrs

    @output_attrs.setter
    def output_attrs(self, output_attrs: List):
        self.__output_attrs = output_attrs
