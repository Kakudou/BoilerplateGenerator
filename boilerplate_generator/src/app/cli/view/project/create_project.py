"""This module handle the form and create a project from it"""
from sys import\
    exit

import questionary
from prompt_toolkit.shortcuts\
    import CompleteStyle

from boilerplate_generator.src.app.adapter\
    .project.create_project.create_project_adapter\
    import CreateProjectAdapter

from boilerplate_generator.src.app.cli.entity_view.project.project_view\
    import ProjectView


class CreateProject:

    def show(self):
        answers = questionary.form(
            name=questionary.text(
                "What's the project name?",
                validate=lambda val: "That project need a name!"
                if len(val) == 0 else True,
            ),
            path=questionary.path(
                "What's the path for this project?",
                complete_style=CompleteStyle.MULTI_COLUMN,
                validate=lambda val: "That project need to be somewhere!"
                if len(val) == 0 else True,
                only_directories=True,
            ),
            types=questionary.checkbox(
                "What types of project this will be?",
                choices=["web", "cli", "api"],
                use_pointer=True,
            ),
        ).ask()

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            self.show()

        contract = CreateProjectAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        project = ProjectView.from_contract(contract)
        print(f"The project {project.name} has been created.")
        exit(0)
