"""This module handle the form and show a entity from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .entity.delete_entity.delete_entity_adapter\
    import DeleteEntityAdapter

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class DeleteEntity:

    @staticmethod
    def show(wanted_project=None, wanted_entity=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        entity_name = Factory.select_entity(project_name, wanted_entity, ifr.save_path)

        if entity_name is None:
            print(f"\r\nWhoups, we found no entity in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["project_name"] = project_name
        inputs["name"] = entity_name

        contract = DeleteEntityAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        if contract.deleted:
            print(f"The entity {entity_name} has been deleted.")

        exit(0)
