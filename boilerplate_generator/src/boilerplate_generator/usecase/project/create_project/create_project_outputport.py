""""This module define the output contract to create a CreateProject"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class CreateProjectOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    name: str
        The name of the project
    path: str
        The path of the project
    types: List[str]
        The type of the project

    """

    error: str = None
    name: str = None
    path: str = None
    types: List[str] = None
