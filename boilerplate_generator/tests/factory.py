""" This factory will be used to quickly generate context for the test """
from typing\
    import Dict


class Factory:

    @staticmethod
    def create_project(name: str) -> Dict:
        """Will create a project based on the name """
        project = {}

        project["name"] = f"{name}"
        project["path"] = "/tmp"
        project["types"] = ["cli", "web", "api"]

        return project

    @staticmethod
    def create_feature(name: str) -> Dict:
        """Will create a feature based on the name """
        feature = {}

        feature["name"] = f"{name}"
        feature["type_"] = "cli"
        feature["description"] = "Description for the feature"
        feature["scenario"] = "Description for the scenario"
        feature["given"] = "Given for the scenario"
        feature["when"] = "When for the scenario"
        feature["then"] = "Then for the scenario"

        return feature

    @staticmethod
    def create_constraint(name: str) -> Dict:
        """Will create a constraint based on the name """
        constraint = {}

        constraint["name"] = f"{name}"
        constraint["type_"] = "cli"
        constraint["description"] = "Description for the constraint"
        constraint["scenario"] = "Description for the scenario"
        constraint["given"] = "Given for the scenario"
        constraint["when"] = "When for the scenario"
        constraint["then"] = "Then for the scenario"

        return constraint

    @staticmethod
    def create_entity(name: str) -> Dict:
        """Will create an entity based on the name """
        entity = {}

        entity["name"] = f"{name}"
        entity["domain"] = "DomainEntity"
        entity["attributes"] = [{
            "name": "attr1",
            "description": "desc attr1",
            "type": "str",
            "identifier": True,
        }, {
            "name": "attr2",
            "description": "desc attr2",
            "type": "int",
            "identifier": False,
        }, {
            "name": "attr3",
            "description": "desc attr3",
            "type": "List",
            "identifier": False,
        }]

        return entity

    @staticmethod
    def create_usecase(name: str) -> Dict:
        """Will create an usecase based on the name """
        usecase = {}

        usecase["name"] = f"{name}"
        usecase["description"] = "Description for the usecase"
        usecase["type_"] = "Custom"
        usecase["input_attrs"] = [{
            "name": "attr1",
            "description": "desc attr1",
            "type": "str",
            "identifier": True,
        }, {
            "name": "attr2",
            "description": "desc attr2",
            "type": "int",
            "identifier": False,
        }, {
            "name": "attr3",
            "description": "desc attr3",
            "type": "List",
            "identifier": False,
        }]
        usecase["output_attrs"] = [{
            "name": "attr4",
            "description": "desc attr4",
            "type": "str",
            "identifier": True,
        }, {
            "name": "attr5",
            "description": "desc attr5",
            "type": "int",
            "identifier": False,
        }, {
            "name": "attr6",
            "description": "desc attr6",
            "type": "List",
            "identifier": False,
        }]

        return usecase
