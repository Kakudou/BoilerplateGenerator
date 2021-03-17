""""This module define the input contract to create a ReadEntity"""
from dataclasses\
    import dataclass


@dataclass
class ReadEntityInputPort:
    """"This class define the necessary attributes to create a Entity

    Attributes:
    -----------
    project_name: str
        The name of the project
    name: str
        The name of the entity

    """

    project_name: str = None
    name: str = None
