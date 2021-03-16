""""This module define the output contract to create a ListConstraint"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ListConstraintOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    all_constraints: List[str]
        List of all constraints

    """

    error: str = None
    all_constraints: List[str] = None
