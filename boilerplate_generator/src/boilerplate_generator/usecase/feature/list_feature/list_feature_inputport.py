""""This module define the input contract to create a ListFeature"""
from dataclasses\
    import dataclass


@dataclass
class ListFeatureInputPort:
    """"This class define the necessary attributes to create a Feature

    Attributes:
    -----------
    project_name: str
        The name of the project

    """
    project_name: str = None
