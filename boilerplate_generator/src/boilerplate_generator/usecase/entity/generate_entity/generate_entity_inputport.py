""""This module define the input contract to create a GenerateEntity"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class GenerateEntityInputPort:
    """"This class define the necessary attributes to create a Entity

    Attributes:
    -----------
    entity_name: str
        The name of the entity
    force: bool
        Force the generation
    project_name: str
        The name of the project
    project_path: str
        The path of the project
    project_types: List[str]
        The type of the project

    """

    entity_name: str = None

    force: bool = None

    project_name: str = None

    project_path: str = None

    project_types: List[str] = None
