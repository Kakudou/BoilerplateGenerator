""""This module define the output contract to create a CreateFeature"""
from dataclasses\
    import dataclass


@dataclass
class CreateFeatureOutputPort:
    """This class defined the attributes the adapter will get

    Attributes:
    -----------
    error: str
        if an error happened during the usecase
    name: str
        The name of the feature
    project_name: str
        The name of the project
    type_: str
        The type_ of the feature
    domain: str
        The domain of the feature
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

    error: str = None
    name: str = None
    project_name: str = None
    type_: str = None
    domain: str = None
    description: str = None
    scenario: str = None
    given: str = None
    when: str = None
    then: str = None
