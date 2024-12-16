"""This module handle the form and show a project from it"""
from sys import\
    exit

import re
import questionary

from boilerplate_generator.src.app.adapter\
    .project.read_project.read_project_adapter\
    import ReadProjectAdapter
from boilerplate_generator.src.app.cli.entity_view.project.project_view\
    import ProjectView

from boilerplate_generator.src.app.adapter\
    .constraint.create_constraint.create_constraint_adapter\
    import CreateConstraintAdapter
from boilerplate_generator.src.app.cli.entity_view.constraint.constraint_view\
    import ConstraintView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class CreateConstraint:

    @staticmethod
    def show(wanted_project=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        project_inputs = {}
        project_inputs["name"] = project_name

        contract = ReadProjectAdapter.execute(project_inputs)
        project = ProjectView.from_contract(contract)

        inputs = Factory.create_constraint_form(None, project.types)

        if inputs["type_"] == "core":
            snakename = re.sub(r'(?!^)([A-Z]+)', r'_\1', project.name).lower()
            inputs["type_"] = snakename
        inputs["project_name"] = project_name

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            CreateConstraint.show(wanted_project, file_dir)

        contract = CreateConstraintAdapter.execute(inputs)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        constraint = ConstraintView.from_contract(contract)
        print(f"The constraint {constraint.name} has been created.")

        exit(0)
