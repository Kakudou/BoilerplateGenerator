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
        print(f"\r\nThe constraint 'Name' is: {constraint.name}")
        print(f"The constraint 'Type' is: {constraint.type_}")
        print(f"The constraint 'Domain' is: {constraint.domain}")
        print(f"The constraint 'Description' is: {constraint.description}")
        print(f"The constraint 'Scenario' is: {constraint.scenario}")
        print(f"The constraint 'Given' is: {constraint.given}")
        print(f"The constraint 'When' is: {constraint.when}")
        print(f"The constraint 'Then' is: {constraint.then}")

        exit(0)
