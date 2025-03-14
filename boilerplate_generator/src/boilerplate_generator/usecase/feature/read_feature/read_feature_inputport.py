""""This module define the input contract to create a ReadFeature"""
from dataclasses\
    import dataclass


@dataclass
class ReadFeatureInputPort:
    """"This class define the necessary attributes to create a Feature

    Attributes:
    -----------
    name: str
        The name of the feature
    project_name: str
        The name of the project

    """

    name: str = None
    project_name: str = None
