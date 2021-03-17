""""This module define the input contract to create a ReadUsecase"""
from dataclasses\
    import dataclass


@dataclass
class ReadUsecaseInputPort:
    """"This class define the necessary attributes to create a Usecase

    Attributes:
    -----------
    name: str
        The name of the usecase
    project_name: str
        The name of the project

    """

    name: str = None
    project_name: str = None
