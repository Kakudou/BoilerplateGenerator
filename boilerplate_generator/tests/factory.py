""" This factory will be used to quickly generate context for the test """
from typing\
    import Dict

class Factory:

    @classmethod
    def create_project(cls, name: str) -> Dict:
        """Will create a project based on the name """
        project = {}

        project["name"] = f"Name{name}"
        project["path"] = "/tmp"
        project["types"] = ["cli", "web", "api"]

        return project
