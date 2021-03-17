"""This module handle the form and create a project from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .project.create_project.create_project_adapter\
    import CreateProjectAdapter

from boilerplate_generator.src.app.cli.entity_view.project.project_view\
    import ProjectView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory


class CreateProject:

    @staticmethod
    def show():

        answers = Factory.create_project_form()

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            CreateProject.show()

        contract = CreateProjectAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        project = ProjectView.from_contract(contract)
        print(f"The project {project.name} has been created.")
        exit(0)
