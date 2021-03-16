""""This module define the input contract to create a ListConstraint"""
from dataclasses\
    import dataclass


@dataclass
class ListConstraintInputPort:
    """"This class define the necessary attributes to create a Constraint

    Attributes:
    -----------
    project_name: str
        The name of the project

    """
    project_name: str = None
