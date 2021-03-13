""""This module define the input contract to create a DeleteProject"""
from dataclasses\
    import dataclass


@dataclass
class DeleteProjectInputPort:
    """"This class define the necessary attributes to create a Project

    Attributes:
    -----------
    name: str
        The name of the project

    """

    name: str = None
