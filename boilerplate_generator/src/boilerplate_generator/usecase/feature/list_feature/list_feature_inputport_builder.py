"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.list_feature.list_feature_inputport\
    import ListFeatureInputPort


@dataclass
class ListFeatureInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: ListFeatureInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_project_name: str
        fill the project_name in the contract
    build:
        build the final input contract

    """

    __input: Any = None

    def create(self):
        """ This function create the empty contract

        Returns:
        --------
        ListFeatureInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = ListFeatureInputPort()
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the ListFeature

        Returns:
        --------
        ListFeatureOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def build(self) -> ListFeatureInputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListFeatureInputPort
            the contract filled

        """

        return self.__input
