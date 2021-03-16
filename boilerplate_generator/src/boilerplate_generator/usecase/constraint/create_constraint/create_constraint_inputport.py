""""This module define the input contract to create a CreateConstraint"""
from dataclasses\
    import dataclass


@dataclass
class CreateConstraintInputPort:
    """"This class define the necessary attributes to create a Constraint

    Attributes:
    -----------
    name: str
        The name of the constraint
    project_name: str
        The name of the project
    description: str
        The description of the constraint
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
