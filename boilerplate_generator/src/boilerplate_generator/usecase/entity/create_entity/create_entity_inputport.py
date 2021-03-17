""""This module define the input contract to create a CreateEntity"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class CreateEntityInputPort:
    """"This class define the necessary attributes to create a Entity

    Attributes:
    -----------
    project_name: str
        The name of the project
    name: str
        The name of the entity
    domain: str
        The domain of the entity
    attributes: List
        The attributes owned by the entity

    """

    project_name: str = None
    name: str = None
    domain: str = None
    attributes: List = None
