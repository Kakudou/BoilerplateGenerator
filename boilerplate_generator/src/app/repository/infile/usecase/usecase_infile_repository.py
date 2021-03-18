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
    dto.usecase.usecase_dto\
    import UsecaseDTO
from boilerplate_generator.src.boilerplate_generator.gateway.\
    usecase.usecase_gateway\
    import UsecaseGateway
from boilerplate_generator.src.boilerplate_generator.entity.\
    usecase.usecase\
    import Usecase
from boilerplate_generator.src.app.\
    repository.infile.infile_persist\
    import InFilePersist


@Singleton
class UsecaseINFILERepository(UsecaseGateway):
    """"This class implement the UsecaseGateway

    Functions:
    ----------
    __init__:
        will get the dict from InFilePersist
    _generate_id:
        will generate an hash from identifier for storage
    save:
        will 'save' the Usecase infile dict
    exist_by_identifier:
        will check if an Usecase with this identifier exist
    update_by_identifier:
        will 'update' the Usecase infile dict
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
        yaml = usecase_dto.to_yaml()

        file_dest = f"{self.__persists.save_path}/{usecase_dto.project_name}.yml"

        with open(file_dest, "r") as file:
            yaml_to_dict = load(file, Loader=FullLoader)

        if "usecases" not in yaml_to_dict["project"].keys():
            yaml_to_dict["project"]["usecases"] = {}

        yaml_to_dict["project"]["usecases"][usecase_dto.name] = yaml

        with open(file_dest, "w") as file:
            dump(yaml_to_dict, file, Dumper=Dumper)

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "usecases" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["usecases"].keys():
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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "usecases" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["usecases"].keys():
                    yaml_to_dict["project"]["usecases"][identifier[0]]["description"] = usecase.description
                    yaml_to_dict["project"]["usecases"][identifier[0]]["type_"] = usecase.type_
                    yaml_to_dict["project"]["usecases"][identifier[0]]["input_attrs"] = usecase.input_attrs
                    yaml_to_dict["project"]["usecases"][identifier[0]]["output_attrs"] = usecase.output_attrs

                    with open(file_dest, "w") as file:
                        dump(yaml_to_dict, file, Dumper=Dumper)

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

        raise NotImplementedError

        return usecase_names

    def find_all_by_project(self, project_name) -> List[str]:
        """This function will find all usecase for a project

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

        file_dest = f"{self.__persists.save_path}/{project_name}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "usecases" in yaml_to_dict["project"].keys():
                for usecase in yaml_to_dict["project"]["usecases"]:
                    all_usecases.append(usecase)

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

        file_dest = f"{self.__persists.save_path}/{project_name}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "usecases" in yaml_to_dict["project"].keys():
                for usecase in yaml_to_dict["project"]["usecases"]:
                    if entity_name == yaml_to_dict["project"]["usecases"][usecase]["entity"]:
                        all_usecases.append(usecase)

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "usecases" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["usecases"].keys():
                    usecase_dto = UsecaseDTO()
                    usecase_dto.from_yaml(yaml_to_dict["project"]["usecases"][identifier[0]])

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

        file_dest = f"{self.__persists.save_path}/{identifier[1]}.yml"
        project_exist = path.exists(file_dest)

        if project_exist:
            with open(file_dest, "r") as file:
                yaml_to_dict = load(file, Loader=FullLoader)
            if "usecases" in yaml_to_dict["project"].keys():
                if identifier[0] in yaml_to_dict["project"]["usecases"].keys():
                    del yaml_to_dict["project"]["usecases"][identifier[0]]

                    with open(file_dest, "w") as file:
                        dump(yaml_to_dict, file, Dumper=Dumper)

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


class Dumper(Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
