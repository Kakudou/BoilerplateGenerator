"""This module handle the data access in file"""
from os import path

from hashlib\
    import sha256
from typing\
    import List
from yaml\
    import dump, Dumper, load, FullLoader

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
    repository.infile.infile_persist\
    import InFilePersist


@Singleton
class FeatureINFILERepository(FeatureGateway):
    """"This class implement the FeatureGateway

    Functions:
    ----------
    __init__:
        will get the dict from InFilePersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Feature infile dict
    exist_by_identifier:
        will check if an Feature with this identifier exist
    update_by_identifier:
        will 'update' the Feature infile dict
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
        """Init InFilePersist who will be used for infile storage"""

        self.__persists = InFilePersist()

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
        yaml = feature_dto.to_yaml()

        file_dest = f"{self.__persists.save_path}/{feature_dto.project_name}.yml"

        with open(file_dest, "r") as file:
            yaml_to_dict = load(file, Loader=FullLoader)

        if "features" not in yaml_to_dict["project"].keys():
            yaml_to_dict["project"]["features"] = {}

        yaml_to_dict["project"]["features"][feature_dto.name] = yaml

        with open(file_dest, "w") as file:
            dump(yaml_to_dict, file, Dumper=Dumper)

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "features" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["features"].keys():
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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "features" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["features"].keys():
                    yaml_to_dict["project"]["features"][identifier[0]]["description"] = feature.description
                    yaml_to_dict["project"]["features"][identifier[0]]["scenario"] = feature.scenario
                    yaml_to_dict["project"]["features"][identifier[0]]["given"] = feature.given
                    yaml_to_dict["project"]["features"][identifier[0]]["when"] = feature.when
                    yaml_to_dict["project"]["features"][identifier[0]]["then"] = feature.then

                    with open(file_dest, "w") as file:
                        dump(yaml_to_dict, file, Dumper=Dumper)

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

        raise NotImplementedError

        return feature_names

    def find_all_by_project(self, project_name) -> List[str]:
        """This function will find all feature for a project

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

        file_dest = f"{self.__persists.save_path}/{project_name}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "features" in yaml_to_dict["project"].keys():
                for feature in yaml_to_dict["project"]["features"]:
                    all_features.append(feature)

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "features" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["features"].keys():
                    feature_dto = FeatureDTO()
                    feature_dto.from_yaml(yaml_to_dict["project"]["features"][identifier[0]])

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "features" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["features"].keys():
                    del yaml_to_dict["project"]["features"][identifier[0]]

                    with open(file_dest, "w") as file:
                        dump(yaml_to_dict, file, Dumper=Dumper)

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
        feature.description = feature_dto.description
        feature.scenario = feature_dto.scenario
        feature.given = feature_dto.given
        feature.when = feature_dto.when
        feature.then = feature_dto.then

        return feature


class Dumper(Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
