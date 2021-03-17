""""This module define the input contract to create a UpdateUsecase"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class UpdateUsecaseInputPort:
    """"This class define the necessary attributes to create a Usecase

    Attributes:
    -----------
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

    name: str = None
    description: str = None
    type_: str = None
    entity_name: str = None
    project_name: str = None
    input_attrs: List = None
    output_attrs: List = None
