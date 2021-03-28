""""This module define the input contract to create a GenerateUsecase"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class GenerateUsecaseInputPort:
    """"This class define the necessary attributes to create a Usecase

    Attributes:
    -----------
    usecase_name: str
        The name of the usecase
    entity_name: str
        The name of the entity
    entity_domain: str
        The domain of the entity
    entity_attributes: List[str]
        The attributes of the entity
    project_name: str
        The name of the project
    project_path: str
        The path of the project
    project_types: List[str]
        The type of the project

    """

    usecase_name: str = None
    entity_name: str = None
    entity_domain: str = None
    entity_attributes: List[str] = None
    project_name: str = None
    project_path: str = None
    project_types: List[str] = None
