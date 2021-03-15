"""This module is the builder that ensure the filling of the output contract"""
from dataclasses\
    import dataclass
from typing\
    import Any, List
from boilerplate_generator.src.boilerplate_generator.usecase.\
    feature.list_feature.list_feature_outputport\
    import ListFeatureOutputPort


@dataclass
class ListFeatureOutputPortBuilder:
    """This class defined the function to easily build the output contract

    Attributes:
    -----------
    __output: ListFeatureOutputPort
        the output contract

    Functions:
    ----------
    create:
        create the output contract
    with_all_features: List[str]
        fill the all_features in the contract
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
        ListFeatureOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output = ListFeatureOutputPort()
        return self

    def with_all_features(self, all_features: List[str]):
        """ This function fill the all_features in the contract

        Parameters:
        -----------
        all_features: List[str]
            the all_features of the ListFeature

        Returns:
        --------
        ListFeatureOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.all_features = all_features
        return self

    def with_error(self, error: str):
        """ This function fill the error in the contract

        Parameters:
        -----------
        error: str
            the error of the usecase

        Returns:
        --------
        ListFeatureOutputPortBuilder
            this builder with the contract to fill

        """

        self.__output.error = error
        return self

    def build(self) -> ListFeatureOutputPort:
        """ This function return the filled contract

        Returns:
        --------
        ListFeatureOutputPort
            the contract filled

        """

        return self.__output
