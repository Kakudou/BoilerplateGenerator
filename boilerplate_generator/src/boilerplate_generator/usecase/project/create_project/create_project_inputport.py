""""This module define the input contract to create a CreateProject"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class CreateProjectInputPort:
    """"This class define the necessary attributes to create a Project

    Attributes:
    -----------
    name: str
        The name of the project
    path: str
        The path of the project
    types: List[str]
        The type of the project

    """

    name: str = None
    path: str = None
    types: List[str] = None
