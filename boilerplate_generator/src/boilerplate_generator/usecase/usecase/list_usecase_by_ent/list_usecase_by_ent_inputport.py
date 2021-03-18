""""This module define the input contract to create a ListUsecaseByEnt"""
from dataclasses\
    import dataclass


@dataclass
class ListUsecaseByEntInputPort:
    """"This class define the necessary attributes to create a Usecase

    Attributes:
    -----------
    project_name: str
        The name of the project
    entity_name: str
        The name of the entity

    """

    project_name: str = None
    entity_name: str = None
