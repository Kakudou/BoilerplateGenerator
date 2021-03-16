""""This module define the output contract to create a ReadEntity"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ReadEntityOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    project_name: str
        The name of the project
    name: str
        The name of the entity
    domain: str
        The domain of the entity
    attributes: List
        The attributes owned by the entity

    """

    error: str = None
    project_name: str = None
    name: str = None
    domain: str = None
    attributes: List = None
