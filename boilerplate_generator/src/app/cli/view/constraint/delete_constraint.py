"""This module handle the form and show a constraint from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .constraint.delete_constraint.delete_constraint_adapter\
    import DeleteConstraintAdapter

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class DeleteConstraint:

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

        contract = DeleteConstraintAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        if contract.deleted:
            print(f"The constraint {constraint_name} has been deleted.")

        exit(0)
