""""This module define the output contract to create a ListUsecase"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ListUsecaseOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    all_usecases: List[str]
        List of all usecases

    """

    error: str = None
    all_usecases: List[str] = None
