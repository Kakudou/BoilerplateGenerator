"""This module handle the data access in memory"""
from hashlib\
    import sha256
from typing\
    import List

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
    repository.inmemory.inmemory_persist\
    import InMemoryPersist


@Singleton
class EntityINMEMORYRepository(EntityGateway):
    """"This class implement the EntityGateway

    Functions:
    ----------
    __init__:
        will get the dict from InMemoryPersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Entity inmemory dict
    exist_by_identifier:
        will check if an Entity with this identifier exist
    update_by_identifier:
        will 'update' the Entity inmemory dict
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
        """Init InMemoryPersist who will be used for inmemory storage"""

        self.__persists = InMemoryPersist()
        self.__persists.entities = {}

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
        self.__persists.entities[entity_dto.id] = entity_dto

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

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            found = self.__persists.entities[hash_id]
        except KeyError:
            found = None

        if found is not None:
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

        entity_dto = self._convert_to_dto(entity)
        self.__persists.entities[entity_dto.id] = entity_dto

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
        for entity_id in self.__persists.entities:
            entity_names.append(self.__persists.entities[entity_id].name)

        return entity_names

    def find_all_by_project(self, project_name) -> List[str]:
        """This function will find all Entity for a project

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

        for entity_id in self.__persists.entities:
            all_entities.append(self.__persists.entities[entity_id].name)

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

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            entity_dto = self.__persists.entities[hash_id]
        except KeyError:
            entity_dto = None

        if entity_dto is not None:
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

        entity_id = self._generate_id(identifier)
        del self.__persists.entities[entity_id]

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
