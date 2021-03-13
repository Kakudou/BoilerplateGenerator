"""This module handle the data access in memory"""
from hashlib\
    import sha256
from typing\
    import List

from boilerplate_generator.src.utils.\
    singleton\
    import Singleton
from boilerplate_generator.src.app.\
    dto.project.project_dto\
    import ProjectDTO
from boilerplate_generator.src.boilerplate_generator.gateway.\
    project.project_gateway\
    import ProjectGateway
from boilerplate_generator.src.boilerplate_generator.entity.\
    project.project\
    import Project
from boilerplate_generator.src.app.\
    repository.inmemory.inmemory_persist\
    import InMemoryPersist


@Singleton
class ProjectINMEMORYRepository(ProjectGateway):
    """"This class implement the ProjectGateway

    Functions:
    ----------
    __init__:
        will get the dict from InMemoryPersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Project inmemory dict
    exist_by_identifier:
        will check if an Project with this identifier exist
    update_by_identifier:
        will 'update' the Project inmemory dict
    find_all:
        will search all Project
    find_by_identifier:
        will search an Project by his identifier
    destroy_by_identifier:
        will delete an Project by his identifier
    _convert_to_dto:
        convert core Project to ProjectDTO
    _convert_to_entity:
        convert ProjectDTO to core Project
    """

    def __init__(self):
        """Init InMemoryPersist who will be used for inmemory storage"""

        self.__persists = InMemoryPersist()
        self.__persists.projects = {}

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

    def save(self, project: Project) -> bool:
        """This function will save Project as ProjectDTO

        Parameters:
        -----------
        project: Project
            The Project that we will be saved and convert as ProjectDTO

        Returns:
        --------
        bool
            True if saved

        """

        saved = False

        project_dto = self._convert_to_dto(project)
        self.__persists.projects[project_dto.id] = project_dto

        saved = True

        return saved

    def exist_by_identifier(self, identifier) -> bool:
        """This function will check Project existence by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for the Project to check

        Returns:
        --------
        bool
            True if exist

        """

        exist = False

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            found = self.__persists.projects[hash_id]
        except KeyError:
            found = None

        if found is not None:
            exist = True

        return exist

    def update_by_identifier(self, identifier: str, project: Project) -> bool:
        """This function will update Project

        Parameters:
        -----------
        identifier: str
            the identifier for the Project to update
        project: Project
            The Project that we will be updated

        Returns:
        --------
        bool
            True if updated

        """

        updated = False

        project_dto = self._convert_to_dto(project)
        self.__persists.projects[project_dto.id] = project_dto

        updated = True

        return updated

    def find_all(self) -> List[str]:
        """This function will find all Project

        Parameters:
        -----------

        Returns:
        --------
        List[str]:
            all Project

        """

        project_names = []
        for project_id in self.__persists.projects:
            project_names.append(self.__persists.projects[project_id].name)

        return project_names

    def find_by_identifier(self, identifier: str) -> Project:
        """This function will find Project by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for Project to find

        Returns:
        --------
        Project:
            The Project

        """

        project = None

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            project_dto = self.__persists.projects[hash_id]
        except KeyError:
            project_dto = None

        if project_dto is not None:
            project = self._convert_to_entity(project_dto)

        return project

    def destroy_by_identifier(self, identifier: str) -> bool:
        """This function will delete Project

        Parameters:
        -----------
        identifier: str
            The identifier for the Project to delete

        Returns:
        --------
        bool
            True if deleted

        """

        deleted = False

        project_id = self._generate_id(identifier)
        del self.__persists.projects[project_id]

        deleted = True

        return deleted

    def _convert_to_dto(self, project: Project) -> ProjectDTO:
        """This function will convert Project to a ProjectDTO

        Parameters:
        -----------
        project: Project
            Entity Project as seen by the core

        Returns:
        --------
        ProjectDTO
            the ProjectDTO ready to be persist

        """

        identifier = (project.name)

        project_dto = ProjectDTO()
        project_dto.id = self._generate_id(identifier)
        project_dto.name = project.name
        project_dto.path = project.path
        project_dto.types = project.types

        return project_dto

    def _convert_to_entity(self, project_dto: ProjectDTO) -> Project:
        """This function will convert a ProjectDTO to Project

        Parameters:
        -----------
        ProjectDTO
            the ProjectDTO ready to be persist

        Returns:
        --------
        project: Project
            Entity Project as seen by the core

        """

        project = Project()
        project.name = project_dto.name
        project.path = project_dto.path
        project.types = project_dto.types

        return project
