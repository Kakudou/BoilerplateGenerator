""""This module define the input contract to create a ReadProject"""
from dataclasses\
    import dataclass


@dataclass
class ReadProjectInputPort:
    """"This class define the necessary attributes to create a Project

    Attributes:
    -----------
    name: str
        The name of the project

    """

    name: str = None
