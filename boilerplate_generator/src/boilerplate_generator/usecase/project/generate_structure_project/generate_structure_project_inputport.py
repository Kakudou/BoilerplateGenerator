""""This module define the input contract to create a GenerateStructureProject"""
from dataclasses\
    import dataclass


@dataclass
class GenerateStructureProjectInputPort:
    """"This class define the necessary attributes to create a Project

    Attributes:
    -----------
    project_name: str
        The name of the project
    force: bool
        Force the generation

    """

    project_name: str = None

    force: bool = None
