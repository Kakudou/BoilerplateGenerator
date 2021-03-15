""""This module define the output contract to create a ListFeature"""
from dataclasses\
    import dataclass
from typing\
    import List


@dataclass
class ListFeatureOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    all_features: List[str]
        List of all features

    """

    error: str = None
    all_features: List[str] = None
