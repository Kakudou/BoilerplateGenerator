"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.update_project.update_project_inputport\
    import UpdateProjectInputPort


@dataclass
class UpdateProjectInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: UpdateProjectInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_name: str
        fill the name in the contract
    with_path: str
        fill the path in the contract
    with_types: List[str]
        fill the types in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        UpdateProjectInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = UpdateProjectInputPort()
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the UpdateProject

        Returns:
        --------
        UpdateProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.name = name
        return self

    def with_path(self, path: str):
        """ This function fill the path in the contract

        Parameters:
        -----------
        path: str
            the path of the UpdateProject

        Returns:
        --------
        UpdateProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.path = path
        return self

    def with_types(self, types: List[str]):
        """ This function fill the types in the contract

        Parameters:
        -----------
        types: List[str]
            the types of the UpdateProject

        Returns:
        --------
        UpdateProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.types = types
        return self

    def build(self) -> UpdateProjectInputPort:
        """ This function return the filled contract

        Returns:
        --------
        UpdateProjectInputPort
            the contract filled

        """

        return self.__input
