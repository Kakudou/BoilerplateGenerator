""""This module define the output contract to create a CreateUsecase"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class CreateUsecaseOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    name: str
        The name of the usecase
    description: str
        The description of the usecase
    type_: str
        The type of the usecase CRUDL or custom
    entity_name: str
        The name of the entity
    project_name: str
        The name of the project
    input_attrs: List
        Additional input attributes for the usecase
    output_attrs: List
        Additional output attribute for the usecase

    """

    error: str = None
    name: str = None
    description: str = None
    type_: str = None
    entity_name: str = None
    project_name: str = None
    input_attrs: List = None
    output_attrs: List = None
