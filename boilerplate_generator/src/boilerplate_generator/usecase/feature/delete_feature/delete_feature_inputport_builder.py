"""This module is the builder that ensure the filling of the input contract"""
from dataclasses\
    import dataclass
from typing\
    import Any
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.delete_feature.delete_feature_inputport\
    import DeleteFeatureInputPort


@dataclass
class DeleteFeatureInputPortBuilder:
    """This class defined the function to easily build the input contract

    Attributes:
    -----------
    __input: DeleteFeatureInputPort
        the input contract

    Functions:
    ----------
    create:
        create the input contract
    with_name: str
        fill the name in the contract
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
        DeleteFeatureInputPortBuilder
            this builder with the contract to fill

        """

        self.__input = DeleteFeatureInputPort()
        return self

    def with_name(self, name: str):
        """ This function fill the name in the contract

        Parameters:
        -----------
        name: str
            the name of the DeleteFeature

        Returns:
        --------
        DeleteFeatureOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.name = name
        return self

    def with_project_name(self, project_name: str):
        """ This function fill the project_name in the contract

        Parameters:
        -----------
        project_name: str
            the project_name of the DeleteFeature

        Returns:
        --------
        DeleteFeatureOutputPortBuilder
            this builder with the contract to fill

        """

        self.__input.project_name = project_name
        return self

    def build(self) -> DeleteFeatureInputPort:
        """ This function return the filled contract

        Returns:
        --------
        DeleteFeatureInputPort
            the contract filled

        """

        return self.__input
