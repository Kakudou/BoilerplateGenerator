"""This module handle the data access in memory"""
from hashlib\
    import sha256
from typing\
    import List

from boilerplate_generator.src.utils.\
    singleton\
    import Singleton
from boilerplate_generator.src.app.\
    dto.usecase.usecase_dto\
    import UsecaseDTO
from boilerplate_generator.src.boilerplate_generator.gateway.\
    usecase.usecase_gateway\
    import UsecaseGateway
from boilerplate_generator.src.boilerplate_generator.entity.\
    usecase.usecase\
    import Usecase
from boilerplate_generator.src.app.\
    repository.inmemory.inmemory_persist\
    import InMemoryPersist


@Singleton
class UsecaseINMEMORYRepository(UsecaseGateway):
    """"This class implement the UsecaseGateway

    Functions:
    ----------
    __init__:
        will get the dict from InMemoryPersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Usecase inmemory dict
    exist_by_identifier:
        will check if an Usecase with this identifier exist
    update_by_identifier:
        will 'update' the Usecase inmemory dict
    find_all:
        will search all Usecase
    find_by_identifier:
        will search an Usecase by his identifier
    destroy_by_identifier:
        will delete an Usecase by his identifier
    _convert_to_dto:
        convert core Usecase to UsecaseDTO
    _convert_to_entity:
        convert UsecaseDTO to core Usecase
    """

    def __init__(self):
        """Init InMemoryPersist who will be used for inmemory storage"""

        self.__persists = InMemoryPersist()
        self.__persists.usecases = {}

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

    def save(self, usecase: Usecase) -> bool:
        """This function will save Usecase as UsecaseDTO

        Parameters:
        -----------
        usecase: Usecase
            The Usecase that we will be saved and convert as UsecaseDTO

        Returns:
        --------
        bool
            True if saved

        """

        saved = False

        usecase_dto = self._convert_to_dto(usecase)
        self.__persists.usecases[usecase_dto.id] = usecase_dto

        saved = True

        return saved

    def exist_by_identifier(self, identifier) -> bool:
        """This function will check Usecase existence by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for the Usecase to check

        Returns:
        --------
        bool
            True if exist

        """

        exist = False

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            found = self.__persists.usecases[hash_id]
        except KeyError:
            found = None

        if found is not None:
            exist = True

        return exist

    def update_by_identifier(self, identifier: str, usecase: Usecase) -> bool:
        """This function will update Usecase

        Parameters:
        -----------
        identifier: str
            the identifier for the Usecase to update
        usecase: Usecase
            The Usecase that we will be updated

        Returns:
        --------
        bool
            True if updated

        """

        updated = False

        usecase_dto = self._convert_to_dto(usecase)
        self.__persists.usecases[usecase_dto.id] = usecase_dto

        updated = True

        return updated

    def find_all(self) -> List[str]:
        """This function will find all Usecase

        Parameters:
        -----------

        Returns:
        --------
        List[str]:
            all Usecase

        """

        usecase_names = []
        for usecase_id in self.__persists.usecases:
            usecase_names.append(self.__persists.usecases[usecase_id].name)

        return usecase_names

    def find_all_by_project(self, project_name) -> List[str]:
        """This function will find all Usecase for a project

        Parameters:
        -----------
        project_name: str
            the name of the project

        Returns:
        --------
        List[str]:
            all entities Usecase

        """
        all_usecases = []

        for usecase_id in self.__persists.usecases:
            all_usecases.append(self.__persists.usecases[usecase_id].name)

        return all_usecases

    def find_all_by_entity(self, project_name, entity_name) -> List[str]:
        """This function will find all Usecase for a project for an entity.

        Parameters:
        -----------
        project_name: str
            the name of the project
        entity_name: str
            the name of the entity

        Returns:
        --------
        List[str]:
            all entities Usecase

        """
        all_usecases = []

        for usecase_id in self.__persists.usecases:
            if entity_name == self.__persists.usecases[usecase_id].entity_name:
                all_usecases.append(self.__persists.usecases[usecase_id].name)

        return all_usecases

    def find_by_identifier(self, identifier: str) -> Usecase:
        """This function will find Usecase by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for Usecase to find

        Returns:
        --------
        Usecase:
            The Usecase

        """

        usecase = None

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            usecase_dto = self.__persists.usecases[hash_id]
        except KeyError:
            usecase_dto = None

        if usecase_dto is not None:
            usecase = self._convert_to_entity(usecase_dto)

        return usecase

    def destroy_by_identifier(self, identifier: str) -> bool:
        """This function will delete Usecase

        Parameters:
        -----------
        identifier: str
            The identifier for the Usecase to delete

        Returns:
        --------
        bool
            True if deleted

        """

        deleted = False

        usecase_id = self._generate_id(identifier)
        del self.__persists.usecases[usecase_id]

        deleted = True

        return deleted

    def _convert_to_dto(self, usecase: Usecase) -> UsecaseDTO:
        """This function will convert Usecase to a UsecaseDTO

        Parameters:
        -----------
        usecase: Usecase
            Entity Usecase as seen by the core

        Returns:
        --------
        UsecaseDTO
            the UsecaseDTO ready to be persist

        """

        identifier = (usecase.name, usecase.project_name)

        usecase_dto = UsecaseDTO()
        usecase_dto.id = self._generate_id(identifier)
        usecase_dto.name = usecase.name
        usecase_dto.description = usecase.description
        usecase_dto.type_ = usecase.type_
        usecase_dto.entity_name = usecase.entity_name
        usecase_dto.project_name = usecase.project_name
        usecase_dto.input_attrs = usecase.input_attrs
        usecase_dto.output_attrs = usecase.output_attrs

        return usecase_dto

    def _convert_to_entity(self, usecase_dto: UsecaseDTO) -> Usecase:
        """This function will convert a UsecaseDTO to Usecase

        Parameters:
        -----------
        UsecaseDTO
            the UsecaseDTO ready to be persist

        Returns:
        --------
        usecase: Usecase
            Entity Usecase as seen by the core

        """

        usecase = Usecase()
        usecase.name = usecase_dto.name
        usecase.description = usecase_dto.description
        usecase.type_ = usecase_dto.type_
        usecase.entity_name = usecase_dto.entity_name
        usecase.project_name = usecase_dto.project_name
        usecase.input_attrs = usecase_dto.input_attrs
        usecase.output_attrs = usecase_dto.output_attrs

        return usecase
