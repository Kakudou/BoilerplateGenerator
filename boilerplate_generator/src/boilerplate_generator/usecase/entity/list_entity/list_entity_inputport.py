""""This module define the input contract to create a ListEntity"""
from dataclasses\
    import dataclass


@dataclass
class ListEntityInputPort:
    """"This class define the necessary attributes to create a Entity

    Attributes:
    -----------
    project_name: str
        The name of the project

    """

    project_name: str = None
