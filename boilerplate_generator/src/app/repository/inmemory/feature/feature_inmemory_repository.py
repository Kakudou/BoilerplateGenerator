"""This module handle the data access in memory"""
from hashlib\
    import sha256
from typing\
    import List

from boilerplate_generator.src.utils.\
    singleton\
    import Singleton
from boilerplate_generator.src.app.\
    dto.feature.feature_dto\
    import FeatureDTO
from boilerplate_generator.src.boilerplate_generator.gateway.\
    feature.feature_gateway\
    import FeatureGateway
from boilerplate_generator.src.boilerplate_generator.entity.\
    feature.feature\
    import Feature
from boilerplate_generator.src.app.\
    repository.inmemory.inmemory_persist\
    import InMemoryPersist


@Singleton
class FeatureINMEMORYRepository(FeatureGateway):
    """"This class implement the FeatureGateway

    Functions:
    ----------
    __init__:
        will get the dict from InMemoryPersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Feature inmemory dict
    exist_by_identifier:
        will check if an Feature with this identifier exist
    update_by_identifier:
        will 'update' the Feature inmemory dict
    find_all:
        will search all Feature
    find_by_identifier:
        will search an Feature by his identifier
    destroy_by_identifier:
        will delete an Feature by his identifier
    _convert_to_dto:
        convert core Feature to FeatureDTO
    _convert_to_entity:
        convert FeatureDTO to core Feature
    """

    def __init__(self):
        """Init InMemoryPersist who will be used for inmemory storage"""

        self.__persists = InMemoryPersist()
        self.__persists.features = {}

    def _generate_id(self, identifier) -> str:
        """This function will generate an ID for the entity
        base on his identifier

        Returns:
        --------
        str
            the identifier hash

        """
        id = sha256(str(identifier).encode()).hexdigest()

        return id

    def save(self, feature: Feature) -> bool:
        """This function will save Feature as FeatureDTO

        Parameters:
        -----------
        feature: Feature
            The Feature that we will be saved and convert as FeatureDTO

        Returns:
        --------
        bool
            True if saved

        """

        saved = False

        feature_dto = self._convert_to_dto(feature)
        self.__persists.features[feature_dto.id] = feature_dto

        saved = True

        return saved

    def exist_by_identifier(self, identifier) -> bool:
        """This function will check Feature existence by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for the Feature to check

        Returns:
        --------
        bool
            True if exist

        """

        exist = False

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            found = self.__persists.features[hash_id]
        except KeyError:
            found = None

        if found is not None:
            exist = True

        return exist

    def update_by_identifier(self, identifier: str, feature: Feature) -> bool:
        """This function will update Feature

        Parameters:
        -----------
        identifier: str
            the identifier for the Feature to update
        feature: Feature
            The Feature that we will be updated

        Returns:
        --------
        bool
            True if updated

        """

        updated = False

        feature_dto = self._convert_to_dto(feature)
        self.__persists.features[feature_dto.id] = feature_dto

        updated = True

        return updated

    def find_all(self) -> List[str]:
        """This function will find all Feature

        Parameters:
        -----------

        Returns:
        --------
        List[str]:
            all Feature

        """

        feature_names = []
        for feature_id in self.__persists.features:
            feature_names.append(self.__persists.features[feature_id].name)

        return feature_names

    def find_all_by_project(self, project_name) -> List[str]:
        """This function will find all Feature for a project

        Parameters:
        -----------
        project_name: str
            the name of the project

        Returns:
        --------
        List[str]:
            all entities Feature

        """
        all_features = []

        for feature_id in self.__persists.features:
            all_features.append(self.__persists.features[feature_id].name)

        return all_features

    def find_by_identifier(self, identifier: str) -> Feature:
        """This function will find Feature by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for Feature to find

        Returns:
        --------
        Feature:
            The Feature

        """

        feature = None

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            feature_dto = self.__persists.features[hash_id]
        except KeyError:
            feature_dto = None

        if feature_dto is not None:
            feature = self._convert_to_entity(feature_dto)

        return feature

    def destroy_by_identifier(self, identifier: str) -> bool:
        """This function will delete Feature

        Parameters:
        -----------
        identifier: str
            The identifier for the Feature to delete

        Returns:
        --------
        bool
            True if deleted

        """

        deleted = False

        feature_id = self._generate_id(identifier)
        del self.__persists.features[feature_id]

        deleted = True

        return deleted

    def _convert_to_dto(self, feature: Feature) -> FeatureDTO:
        """This function will convert Feature to a FeatureDTO

        Parameters:
        -----------
        feature: Feature
            Entity Feature as seen by the core

        Returns:
        --------
        FeatureDTO
            the FeatureDTO ready to be persist

        """

        identifier = (feature.name, feature.project_name)

        feature_dto = FeatureDTO()
        feature_dto.id = self._generate_id(identifier)
        feature_dto.name = feature.name
        feature_dto.project_name = feature.project_name
        feature_dto.type_ = feature.type_
        feature_dto.description = feature.description
        feature_dto.scenario = feature.scenario
        feature_dto.given = feature.given
        feature_dto.when = feature.when
        feature_dto.then = feature.then

        return feature_dto

    def _convert_to_entity(self, feature_dto: FeatureDTO) -> Feature:
        """This function will convert a FeatureDTO to Feature

        Parameters:
        -----------
        FeatureDTO
            the FeatureDTO ready to be persist

        Returns:
        --------
        feature: Feature
            Entity Feature as seen by the core

        """

        feature = Feature()
        feature.name = feature_dto.name
        feature.project_name = feature_dto.project_name
        feature.type_ = feature_dto.type_
        feature.description = feature_dto.description
        feature.scenario = feature_dto.scenario
        feature.given = feature_dto.given
        feature.when = feature_dto.when
        feature.then = feature_dto.then

        return feature
