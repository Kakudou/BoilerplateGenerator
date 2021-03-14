"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.generate_structure_project.generate_structure_project_inputport\
    import GenerateStructureProjectInputPort


@dataclass
class GenerateStructureProjectInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: GenerateStructureProjectInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_project_name: str
        fill the project_name in the contract
    with_force: bool
        fill the force in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        GenerateStructureProjectInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = GenerateStructureProjectInputPort()
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the GenerateStructureProject

        Returns:
        --------
        GenerateStructureProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def with_force(self, force: bool):
        """ This function fill the force in the contract

        Parameters:
        -----------
        force: bool
            the force of the GenerateStructureProject

        Returns:
        --------
        GenerateStructureProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.force = force
        return self

    def build(self) -> GenerateStructureProjectInputPort:
        """ This function return the filled contract

        Returns:
        --------
        GenerateStructureProjectInputPort
            the contract filled

        """

        return self.__input
