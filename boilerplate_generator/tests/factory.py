""" This factory will be used to quickly generate context for the test """
from typing\
    import Dict


class Factory:

    @staticmethod
    def create_project(name: str) -> Dict:
        """Will create a project based on the name """
        project = {}

        project["name"] = f"Name{name}"
        project["path"] = "/tmp"
        project["types"] = ["cli", "web", "api"]

        return project

    @staticmethod
    def create_feature(name: str) -> Dict:
        """Will create a feature based on the name """
        feature = {}

        feature["name"] = f"Name{name}"
        feature["description"] = "Description for the feature"
        feature["scenario"] = "Description for the scenario"
        feature["given"] = "Given for the scenario"
        feature["when"] = "When for the scenario"
        feature["then"] = "Then for the scenario"

        return feature
