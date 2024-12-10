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
    dto.constraint.constraint_dto\
    import ConstraintDTO
from boilerplate_generator.src.boilerplate_generator.gateway.\
    constraint.constraint_gateway\
    import ConstraintGateway
from boilerplate_generator.src.boilerplate_generator.entity.\
    constraint.constraint\
    import Constraint
from boilerplate_generator.src.app.\
    repository.infile.infile_persist\
    import InFilePersist


@Singleton
class ConstraintINFILERepository(ConstraintGateway):
    """"This class implement the ConstraintGateway

    Functions:
    ----------
    __init__:
        will get the dict from InFilePersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Constraint infile dict
    exist_by_identifier:
        will check if an Constraint with this identifier exist
    update_by_identifier:
        will 'update' the Constraint infile dict
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
        yaml = constraint_dto.to_yaml()

        file_dest = f"{self.__persists.save_path}/{constraint_dto.project_name}.yml"

        with open(file_dest, "r") as file:
            yaml_to_dict = load(file, Loader=FullLoader)

        if "constraints" not in yaml_to_dict["project"].keys():
            yaml_to_dict["project"]["constraints"] = {}

        yaml_to_dict["project"]["constraints"][constraint_dto.name] = yaml

        with open(file_dest, "w") as file:
            dump(yaml_to_dict, file, Dumper=Dumper)

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "constraints" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["constraints"].keys():
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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "constraints" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["constraints"].keys():
                    yaml_to_dict["project"]["constraints"][identifier[0]]["type"] = constraint.type_
                    yaml_to_dict["project"]["constraints"][identifier[0]]["type"] = constraint.domain
                    yaml_to_dict["project"]["constraints"][identifier[0]]["description"] = constraint.description
                    yaml_to_dict["project"]["constraints"][identifier[0]]["scenario"] = constraint.scenario
                    yaml_to_dict["project"]["constraints"][identifier[0]]["given"] = constraint.given
                    yaml_to_dict["project"]["constraints"][identifier[0]]["when"] = constraint.when
                    yaml_to_dict["project"]["constraints"][identifier[0]]["then"] = constraint.then

                    with open(file_dest, "w") as file:
                        dump(yaml_to_dict, file, Dumper=Dumper)

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

        raise NotImplementedError

        return constraint_names

    def find_all_by_project(self, project_name) -> List[str]:
        """This function will find all constraint for a project

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

        file_dest = f"{self.__persists.save_path}/{project_name}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "constraints" in yaml_to_dict["project"].keys():
                for constraint in yaml_to_dict["project"]["constraints"]:
                    all_constraints.append(constraint)

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "constraints" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["constraints"].keys():
                    constraint_dto = ConstraintDTO()
                    constraint_dto.from_yaml(yaml_to_dict["project"]["constraints"][identifier[0]])

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "constraints" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["constraints"].keys():
                    del yaml_to_dict["project"]["constraints"][identifier[0]]

                    with open(file_dest, "w") as file:
                        dump(yaml_to_dict, file, Dumper=Dumper)

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
        constraint_dto.type_ = constraint.type_
        constraint_dto.domain = constraint.domain
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
        constraint.type_ = constraint_dto.type_
        constraint.domain = constraint_dto.domain
        constraint.description = constraint_dto.description
        constraint.scenario = constraint_dto.scenario
        constraint.given = constraint_dto.given
        constraint.when = constraint_dto.when
        constraint.then = constraint_dto.then

        return constraint


class Dumper(Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
