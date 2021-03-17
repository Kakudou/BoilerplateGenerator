""""This module define the input contract to create a CreateFeature"""
from dataclasses\
    import dataclass


@dataclass
class CreateFeatureInputPort:
    """"This class define the necessary attributes to create a Feature

    Attributes:
    -----------
    name: str
        The name of the feature
    project_name: str
        The name of the project
    description: str
        The description of the feature
    scenario: str
        The description of the scenario
    given: str
        The given of the scenario
    when: str
        The when of the scenario
    then: str
        The then of the scenario

    """

    name: str = None
    project_name: str = None
    description: str = None
    scenario: str = None
    given: str = None
    when: str = None
    then: str = None
