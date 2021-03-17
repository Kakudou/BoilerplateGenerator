"""This module handle the form and show a constraint from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .constraint.read_constraint.read_constraint_adapter\
    import ReadConstraintAdapter
from boilerplate_generator.src.app.adapter\
    .constraint.update_constraint.update_constraint_adapter\
    import UpdateConstraintAdapter

from boilerplate_generator.src.app.cli.entity_view.constraint.constraint_view\
    import ConstraintView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class UpdateConstraint:

    @staticmethod
    def show(wanted_project=None, wanted_constraint=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        constraint_name = Factory.select_constraint(project_name, wanted_constraint, ifr.save_path)

        if constraint_name is None:
            print(f"\r\nWhoups, we found no constraint in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["project_name"] = project_name
        inputs["name"] = constraint_name

        contract = ReadConstraintAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        constraint = ConstraintView.from_contract(contract)

        answers = Factory.create_constraint_form(constraint)

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            UpdateConstraint.show()

        answers["project_name"] = project_name
        answers["name"] = constraint_name

        contract = UpdateConstraintAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        constraint = ConstraintView.from_contract(contract)
        print(f"The constraint {constraint.name} has been updated.")
        exit(0)
