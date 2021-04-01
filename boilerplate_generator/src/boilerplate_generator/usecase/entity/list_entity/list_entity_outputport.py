""""This module define the output contract to create a ListEntity"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ListEntityOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    all_entities: List[str]
        List of all entities

    """

    error: str = None
    all_entities: List[str] = None
