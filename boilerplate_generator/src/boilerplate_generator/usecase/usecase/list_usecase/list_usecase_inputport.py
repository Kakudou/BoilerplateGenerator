""""This module define the input contract to create a ListUsecase"""
from dataclasses\
    import dataclass


@dataclass
class ListUsecaseInputPort:
    """"This class define the necessary attributes to create a Usecase

    Attributes:
    -----------
    project_name: str
        The name of the project

    """

    project_name: str = None
