"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.delete_project.delete_project_inputport\
    import DeleteProjectInputPort


@dataclass
class DeleteProjectInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: DeleteProjectInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_name: str
        fill the name in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        DeleteProjectInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = DeleteProjectInputPort()
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the DeleteProject

        Returns:
        --------
        DeleteProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.name = name
        return self

    def build(self) -> DeleteProjectInputPort:
        """ This function return the filled contract

        Returns:
        --------
        DeleteProjectInputPort
            the contract filled

        """

        return self.__input
