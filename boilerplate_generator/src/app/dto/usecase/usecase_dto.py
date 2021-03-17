"""This module is the UsecaseDTO that will be persist"""
from dataclasses\
    import dataclass
from typing\
    import List, Dict


@dataclass
class UsecaseDTO:
    """This class defined the attributes that we want to be persist

    Attributes:
    -----------
    __id: str
        The hash of the identifier of Usecase: (name, project_name)
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

    __id: str = None
    __name: str = None
    __description: str = None
    __type_: str = None
    __entity_name: str = None
    __project_name: str = None
    __input_attrs: List = None
    __output_attrs: List = None

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

    def to_yaml(self) -> Dict[str, str]:
        obj_to_yaml = {
            "name": self.name,
            "description": self.description,
            "type": self.type_,
        }
        if self.input_attrs is not None and len(self.input_attrs) > 0:
            obj_to_yaml["input_attrs"] = self.input_attrs
        if self.output_attrs is not None and len(self.output_attrs) > 0:
            obj_to_yaml["output_attrs"] = self.output_attrs

        return obj_to_yaml

    def from_yaml(self, yaml):
        self.name = yaml["name"]
        self.description = yaml["description"]
        self.type_ = yaml["type"]
        self.input_attrs = yaml["input_attrs"]\
            if "input_attrs" in yaml.keys() else {}
        self.output_attrs = yaml["output_attrs"]\
            if "output_attrs" in yaml.keys() else {}
