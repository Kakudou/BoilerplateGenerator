"""This module handle the data access in memory"""
from hashlib\
    import sha256
from typing\
    import List

from boilerplate_generator.src.utils.\
    singleton\
    import Singleton
from boilerplate_generator.src.app.\
    dto.constraint.constraint_dto\
    import ConstraintDTO
from boilerplate_generator.src.boilerplate_generator.gateway.\
    constraint.constraint_gateway\
    import ConstraintGateway
from boilerplate_generator.src.boilerplate_generator.entity.\
    constraint.constraint\
    import Constraint
from boilerplate_generator.src.app.\
    repository.inmemory.inmemory_persist\
    import InMemoryPersist


@Singleton
class ConstraintINMEMORYRepository(ConstraintGateway):
    """"This class implement the ConstraintGateway

    Functions:
    ----------
    __init__:
        will get the dict from InMemoryPersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Constraint inmemory dict
    exist_by_identifier:
        will check if an Constraint with this identifier exist
    update_by_identifier:
        will 'update' the Constraint inmemory dict
    find_all:
        will search all Constraint
    find_by_identifier:
        will search an Constraint by his identifier
    destroy_by_identifier:
        will delete an Constraint by his identifier
    _convert_to_dto:
        convert core Constraint to ConstraintDTO
    _convert_to_entity:
        convert ConstraintDTO to core Constraint
    """

    def __init__(self):
        """Init InMemoryPersist who will be used for inmemory storage"""

        self.__persists = InMemoryPersist()
        self.__persists.constraints = {}

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

    def save(self, constraint: Constraint) -> bool:
        """This function will save Constraint as ConstraintDTO

        Parameters:
        -----------
        constraint: Constraint
            The Constraint that we will be saved and convert as ConstraintDTO

        Returns:
        --------
        bool
            True if saved

        """

        saved = False

        constraint_dto = self._convert_to_dto(constraint)
        self.__persists.constraints[constraint_dto.id] = constraint_dto

        saved = True

        return saved

    def exist_by_identifier(self, identifier) -> bool:
        """This function will check Constraint existence by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for the Constraint to check

        Returns:
        --------
        bool
            True if exist

        """

        exist = False

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            found = self.__persists.constraints[hash_id]
        except KeyError:
            found = None

        if found is not None:
            exist = True

        return exist

    def update_by_identifier(self, identifier: str, constraint: Constraint) -> bool:
        """This function will update Constraint

        Parameters:
        -----------
        identifier: str
            the identifier for the Constraint to update
        constraint: Constraint
            The Constraint that we will be updated

        Returns:
        --------
        bool
            True if updated

        """

        updated = False

        constraint_dto = self._convert_to_dto(constraint)
        self.__persists.constraints[constraint_dto.id] = constraint_dto

        updated = True

        return updated

    def find_all(self) -> List[str]:
        """This function will find all Constraint

        Parameters:
        -----------

        Returns:
        --------
        List[str]:
            all Constraint

        """

        constraint_names = []
        for constraint_id in self.__persists.constraints:
            constraint_names.append(self.__persists.constraints[constraint_id].name)

        return constraint_names

    def find_all_by_project(self, project_name) -> List[str]:
        """This function will find all Constraint for a project

        Parameters:
        -----------
        project_name: str
            the name of the project

        Returns:
        --------
        List[str]:
            all entities Constraint

        """
        all_constraints = []

        for constraint_id in self.__persists.constraints:
            all_constraints.append(self.__persists.constraints[constraint_id].name)

        return all_constraints

    def find_by_identifier(self, identifier: str) -> Constraint:
        """This function will find Constraint by is identifier

        Parameters:
        -----------
        identifier: str
            The identifier for Constraint to find

        Returns:
        --------
        Constraint:
            The Constraint

        """

        constraint = None

        hash_id = sha256(str(identifier).encode()).hexdigest()

        try:
            constraint_dto = self.__persists.constraints[hash_id]
        except KeyError:
            constraint_dto = None

        if constraint_dto is not None:
            constraint = self._convert_to_entity(constraint_dto)

        return constraint

    def destroy_by_identifier(self, identifier: str) -> bool:
        """This function will delete Constraint

        Parameters:
        -----------
        identifier: str
            The identifier for the Constraint to delete

        Returns:
        --------
        bool
            True if deleted

        """

        deleted = False

        constraint_id = self._generate_id(identifier)
        del self.__persists.constraints[constraint_id]

        deleted = True

        return deleted

    def _convert_to_dto(self, constraint: Constraint) -> ConstraintDTO:
        """This function will convert Constraint to a ConstraintDTO

        Parameters:
        -----------
        constraint: Constraint
            Entity Constraint as seen by the core

        Returns:
        --------
        ConstraintDTO
            the ConstraintDTO ready to be persist

        """

        identifier = (constraint.name, constraint.project_name)

        constraint_dto = ConstraintDTO()
        constraint_dto.id = self._generate_id(identifier)
        constraint_dto.name = constraint.name
        constraint_dto.project_name = constraint.project_name
        constraint_dto.description = constraint.description
        constraint_dto.scenario = constraint.scenario
        constraint_dto.given = constraint.given
        constraint_dto.when = constraint.when
        constraint_dto.then = constraint.then

        return constraint_dto

    def _convert_to_entity(self, constraint_dto: ConstraintDTO) -> Constraint:
        """This function will convert a ConstraintDTO to Constraint

        Parameters:
        -----------
        ConstraintDTO
            the ConstraintDTO ready to be persist

        Returns:
        --------
        constraint: Constraint
            Entity Constraint as seen by the core

        """

        constraint = Constraint()
        constraint.name = constraint_dto.name
        constraint.project_name = constraint_dto.project_name
        constraint.description = constraint_dto.description
        constraint.scenario = constraint_dto.scenario
        constraint.given = constraint_dto.given
        constraint.when = constraint_dto.when
        constraint.then = constraint_dto.then

        return constraint
