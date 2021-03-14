"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    project.list_project.list_project_outputport\
    import ListProjectOutputPort


@dataclass
class ListProjectOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListProjectOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_all_projects: List[str]
        fill the all_projects in the contract
    with_error:
        fill the possible usecase error
    build:
        build the final output contract

    """

    __output: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        ListProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListProjectOutputPort()
        return self

    def with_all_projects(self, all_projects: List[str]):
        """ This function fill the all_projects in the contract

        Parameters:
        -----------
        all_projects: List[str]
            the all_projects of the ListProject

        Returns:
        --------
        ListProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.all_projects = all_projects
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ListProjectOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListProjectOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListProjectOutputPort
            the contract filled

        """

        return self.__output