"""This module handle the form and show a project from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .project.read_project.read_project_adapter\
    import ReadProjectAdapter

from boilerplate_generator.src.app.cli.entity_view.project.project_view\
    import ProjectView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class ReadProject:

    @staticmethod
    def show(wanted_project=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["name"] = project_name

        contract = ReadProjectAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        project = ProjectView.from_contract(contract)
        print(f"\r\nThe project name is: {project.name}")
        print(f"The project path is: {project.path}")
        print(f"The project types are: {', '.join(project.types)}")

        exit(0)
