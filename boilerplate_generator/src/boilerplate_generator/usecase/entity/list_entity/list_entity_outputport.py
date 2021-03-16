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
    all_entitys: List[str]
        List of all entitys

    """

    error: str = None
    all_entitys: List[str] = None
