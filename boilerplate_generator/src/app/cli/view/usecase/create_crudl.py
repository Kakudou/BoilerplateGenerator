"""This module handle the form and show a project from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .usecase.create_usecase.create_usecase_adapter\
    import CreateUsecaseAdapter
from boilerplate_generator.src.app.cli.entity_view.usecase.usecase_view\
    import UsecaseView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class CreateCrudl:

    @staticmethod
    def show(wanted_project=None, wanted_entity=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["project_name"] = project_name

        entity_name = Factory.select_entity(project_name, wanted_entity, ifr.save_path)

        if entity_name is None:
            print(f"\r\nWhoups, we found no entity in: {ifr.save_path}.")
            exit(1)

        print("-----")
        print("")
        confirm = questionary.confirm(
            f"Are you sure you want to generate CRUDL for {entity_name}?",
            default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            CreateCrudl.show(wanted_project, wanted_entity, file_dir)

        inputs["entity_name"] = entity_name
        inputs["project_name"] = project_name
        print("")
        for type_ in ["Create", "Read", "Update", "Delete", "List"]:
            inputs["type_"] = type_
            contract = CreateUsecaseAdapter.execute(inputs)

            if contract.error is not None:
                print(f"Whoups, we got some error here: {contract.error}")
            else:
                usecase = UsecaseView.from_contract(contract)
                print(f"The usecase {usecase.name} has been created.")

        exit(0)
