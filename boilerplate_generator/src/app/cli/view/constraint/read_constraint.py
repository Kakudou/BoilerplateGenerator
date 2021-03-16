"""This module handle the form and show a constraint from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .constraint.read_constraint.read_constraint_adapter\
    import ReadConstraintAdapter

from boilerplate_generator.src.app.cli.entity_view.constraint.constraint_view\
    import ConstraintView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class ReadConstraint:

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
        print(f"\r\nThe constraint 'name' is: {constraint.name}")
        print(f"The constraint 'description' is: {constraint.description}")
        print(f"The constraint 'scenario' is: {constraint.scenario}")
        print(f"The constraint 'given' is: {constraint.given}")
        print(f"The constraint 'when' is: {constraint.when}")
        print(f"The constraint 'then' is: {constraint.then}")

        exit(0)
