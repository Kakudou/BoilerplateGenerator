""""This module define the output contract to create a GenerateUsecase"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class GenerateUsecaseOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    folders: List[str]
        The folders generated
    files: List[str]
        The files generated

    """

    error: str = None
    folders: List[str] = None
    files: List[str] = None
