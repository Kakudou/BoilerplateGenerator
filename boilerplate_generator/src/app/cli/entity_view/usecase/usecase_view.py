"""This module is the Usecase that will be shown"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class UsecaseView:
    """This class defined the attributes that we want to show

    Attributes:
    -----------
    __name: str
        The name of the usecase
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

    @staticmethod
    def from_contract(contract):
        usecase = UsecaseView()
        usecase.name = contract.name
        usecase.description = contract.description
        usecase.type_ = contract.type_
        usecase.entity_name = contract.entity_name
        usecase.project_name = contract.project_name
        usecase.input_attrs = contract.input_attrs
        usecase.output_attrs = contract.output_attrs

        return usecase
