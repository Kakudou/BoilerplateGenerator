"""This module handle the form and show a project from it"""
from sys import\
    exit

import questionary
from questionary\
    import Choice
from prompt_toolkit.shortcuts\
    import CompleteStyle

from boilerplate_generator.src.app.adapter\
    .project.read_project.read_project_adapter\
    import ReadProjectAdapter

from boilerplate_generator.src.app.adapter\
    .project.update_project.update_project_adapter\
    import UpdateProjectAdapter

from boilerplate_generator.src.app.cli.entity_view.project.project_view\
    import ProjectView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class UpdateProject:

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

        choices = ["web", "cli", "api"]
        for choice in project.types:
            choices.remove(choice)
            choices.append(Choice(choice, checked=True))
        choices.reverse()

        answers = questionary.form(
            path=questionary.path(
                "What's the path for this project?",
                complete_style=CompleteStyle.MULTI_COLUMN,
                validate=lambda val: "That project need to be somewhere!"
                if len(val) == 0 else True,
                only_directories=True,
                default=project.path
            ),
            types=questionary.checkbox(
                "What types of project this will be?",
                choices=choices,
                use_pointer=True,
            ),
        ).ask()

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            UpdateProject.show()

        answers["name"] = project_name

        contract = UpdateProjectAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        project = ProjectView.from_contract(contract)
        print(f"The project {project.name} has been updated.")
        exit(0)
