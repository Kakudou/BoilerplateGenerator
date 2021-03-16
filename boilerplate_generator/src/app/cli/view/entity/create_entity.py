"""This module handle the form and show a project from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .entity.create_entity.create_entity_adapter\
    import CreateEntityAdapter
from boilerplate_generator.src.app.cli.entity_view.entity.entity_view\
    import EntityView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class CreateEntity:

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

        inputs["name"] = questionary.text(
            "What's the entity name?",
            validate=lambda val: "That entity need a name!"
            if len(val) == 0 else True,
        ).ask()

        inputs["domain"] = questionary.text(
            "What's the entity domain?",
            validate=lambda val: "That domain need a name!"
            if len(val) == 0 else True,
            default=inputs["name"]
        ).ask()

        inputs["attributes"] = []

        print("")
        create_attr = questionary.confirm(
            "Would you like to add an attribute?", default=True).ask()

        while create_attr:
            attribute = questionary.form(
                name=questionary.text(
                    "What's the attribute name?",
                    validate=lambda val: "That attribute need a name!"
                    if len(val) == 0 else True,
                ),
                description=questionary.text(
                    "What's the attribute description?",
                    validate=lambda val: "That attribute need a description!"
                    if len(val) == 0 else True,
                ),
                type=questionary.text(
                    "What's the attribute type?",
                    default="str"
                ),
                identifier=questionary.confirm(
                    "That attribute should be consider as an identifier?",
                    default=False)
            ).ask()

            inputs["attributes"].append(attribute)
            print("")
            create_attr = questionary.confirm(
                "Would you like to add another attribute?").ask()

        inputs["project_name"] = project_name

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            CreateEntity.show(wanted_project, file_dir)

        contract = CreateEntityAdapter.execute(inputs)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        entity = EntityView.from_contract(contract)
        print(f"The entity {entity.name} has been created.")

        exit(0)
