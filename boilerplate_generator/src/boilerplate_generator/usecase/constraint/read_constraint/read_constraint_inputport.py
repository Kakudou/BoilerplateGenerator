""""This module define the input contract to create a ReadConstraint"""
from dataclasses\
    import dataclass


@dataclass
class ReadConstraintInputPort:
    """"This class define the necessary attributes to create a Constraint

    Attributes:
    -----------
    name: str
        The name of the constraint
    project_name: str
        The name of the project

    """

    name: str = None

    project_name: str = None
