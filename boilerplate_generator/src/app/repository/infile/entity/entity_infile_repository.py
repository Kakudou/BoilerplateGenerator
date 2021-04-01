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
    dto.entity.entity_dto\
    import EntityDTO
from boilerplate_generator.src.boilerplate_generator.gateway.\
    entity.entity_gateway\
    import EntityGateway
from boilerplate_generator.src.boilerplate_generator.entity.\
    entity.entity\
    import Entity
from boilerplate_generator.src.app.\
    repository.infile.infile_persist\
    import InFilePersist


@Singleton
class EntityINFILERepository(EntityGateway):
    """"This class implement the EntityGateway

    Functions:
    ----------
    __init__:
        will get the dict from InFilePersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Entity infile dict
    exist_by_identifier:
        will check if an Entity with this identifier exist
    update_by_identifier:
        will 'update' the Entity infile dict
    find_all:
        will search all Entity
    find_by_identifier:
        will search an Entity by his identifier
    destroy_by_identifier:
        will delete an Entity by his identifier
    _convert_to_dto:
        convert core Entity to EntityDTO
    _convert_to_entity:
        convert EntityDTO to core Entity
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

    def save(self, entity: Entity) -> bool:
        """This function will save Entity as EntityDTO

        Parameters:
        -----------
        entity: Entity
            The Entity that we will be saved and convert as EntityDTO

        Returns:
        --------
        bool
            True if saved

        """

        saved = False

        entity_dto = self._convert_to_dto(entity)
        yaml = entity_dto.to_yaml()

        file_dest = f"{self.__persists.save_path}/{entity_dto.project_name}.yml"

        with open(file_dest, "r") as file:
            yaml_to_dict = load(file, Loader=FullLoader)

        if "entities" not in yaml_to_dict["project"].keys():
            yaml_to_dict["project"]["entities"] = {}

        yaml_to_dict["project"]["entities"][entity_dto.name] = yaml

        with open(file_dest, "w") as file:
            dump(yaml_to_dict, file, Dumper=Dumper)

        saved = True

        return saved

    def exist_by_identifier(self, identifier) -> bool:
        """This function will check Entity existence by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for the Entity to check

        Returns:
        --------
        bool
            True if exist

        """

        exist = False

        file_dest = f"{self.__persists.save_path}/{identifier[0]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "entities" in yaml_to_dict["project"].keys():
                if identifier[1] in yaml_to_dict["project"]["entities"].keys():
                    exist = True

        return exist

    def update_by_identifier(self, identifier: str, entity: Entity) -> bool:
        """This function will update Entity

        Parameters:
        -----------
        identifier: str
            the identifier for the Entity to update
        entity: Entity
            The Entity that we will be updated

        Returns:
        --------
        bool
            True if updated

        """

        updated = False

        file_dest = f"{self.__persists.save_path}/{identifier[0]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "entities" in yaml_to_dict["project"].keys():
                if identifier[1] in yaml_to_dict["project"]["entities"].keys():
                    yaml_to_dict["project"]["entities"][identifier[1]]["domain"] = entity.domain
                    if len(entity.attributes) > 0:
                        yaml_to_dict["project"]["entities"][identifier[1]]["attributes"] = entity.attributes

                    with open(file_dest, "w") as file:
                        dump(yaml_to_dict, file, Dumper=Dumper)

                    updated = True

        return updated

    def find_all(self) -> List[str]:
        """This function will find all Entity

        Parameters:
        -----------

        Returns:
        --------
        List[str]:
            all Entity

        """

        entity_names = []

        raise NotImplementedError

        return entity_names

    def find_all_by_project(self, project_name) -> List[str]:
        """This function will find all entity for a project

        Parameters:
        -----------
        project_name: str
            the name of the project

        Returns:
        --------
        List[str]:
            all entities Entity

        """
        all_entities = []

        file_dest = f"{self.__persists.save_path}/{project_name}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "entities" in yaml_to_dict["project"].keys():
                for entity in yaml_to_dict["project"]["entities"]:
                    all_entities.append(entity)

        return all_entities

    def find_by_identifier(self, identifier: str) -> Entity:
        """This function will find Entity by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for Entity to find

        Returns:
        --------
        Entity:
            The Entity

        """

        entity = None

        file_dest = f"{self.__persists.save_path}/{identifier[0]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "entities" in yaml_to_dict["project"].keys():
                if identifier[1] in yaml_to_dict["project"]["entities"].keys():
                    entity_dto = EntityDTO()
                    entity_dto.from_yaml(yaml_to_dict["project"]["entities"][identifier[1]])

                    entity = self._convert_to_entity(entity_dto)

        return entity

    def destroy_by_identifier(self, identifier: str) -> bool:
        """This function will delete Entity

        Parameters:
        -----------
        identifier: str
            The identifier for the Entity to delete

        Returns:
        --------
        bool
            True if deleted

        """

        deleted = False

        file_dest = f"{self.__persists.save_path}/{identifier[0]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "entities" in yaml_to_dict["project"].keys():
                if identifier[1] in yaml_to_dict["project"]["entities"].keys():
                    del yaml_to_dict["project"]["entities"][identifier[1]]

                    with open(file_dest, "w") as file:
                        dump(yaml_to_dict, file, Dumper=Dumper)

                    deleted = True

        return deleted

    def _convert_to_dto(self, entity: Entity) -> EntityDTO:
        """This function will convert Entity to a EntityDTO

        Parameters:
        -----------
        entity: Entity
            Entity Entity as seen by the core

        Returns:
        --------
        EntityDTO
            the EntityDTO ready to be persist

        """

        identifier = (entity.project_name, entity.name)

        entity_dto = EntityDTO()
        entity_dto.id = self._generate_id(identifier)
        entity_dto.project_name = entity.project_name
        entity_dto.name = entity.name
        entity_dto.domain = entity.domain
        entity_dto.attributes = entity.attributes

        return entity_dto

    def _convert_to_entity(self, entity_dto: EntityDTO) -> Entity:
        """This function will convert a EntityDTO to Entity

        Parameters:
        -----------
        EntityDTO
            the EntityDTO ready to be persist

        Returns:
        --------
        entity: Entity
            Entity Entity as seen by the core

        """

        entity = Entity()
        entity.project_name = entity_dto.project_name
        entity.name = entity_dto.name
        entity.domain = entity_dto.domain
        entity.attributes = entity_dto.attributes

        return entity


class Dumper(Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
