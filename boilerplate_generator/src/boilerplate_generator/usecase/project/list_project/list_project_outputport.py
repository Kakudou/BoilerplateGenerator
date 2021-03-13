""""This module define the output contract to create a ListProject"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ListProjectOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    all_projects: List[str]
        List of all projects

    """

    error: str = None
    all_projects: List[str] = None
