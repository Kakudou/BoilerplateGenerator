"""This module handle the form and show a entity from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .entity.read_entity.read_entity_adapter\
    import ReadEntityAdapter
from boilerplate_generator.src.app.adapter\
    .entity.update_entity.update_entity_adapter\
    import UpdateEntityAdapter

from boilerplate_generator.src.app.cli.entity_view.entity.entity_view\
    import EntityView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class UpdateEntity:

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

        contract = ReadEntityAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        entity = EntityView.from_contract(contract)

        answers = {}
        answers["domain"] = questionary.text(
            "What's the entity domain?",
            validate=lambda val: "That domain need a name!"
            if len(val) == 0 else True,
            default=entity.domain
        ).ask()

        print("\r\nLet see the existing attributes.")
        answers["attributes"] = []
        for attribute in entity.attributes:
            print("")
            attribute = questionary.form(
                name=questionary.text(
                    "What's the attribute name?",
                    validate=lambda val: "That attribute need a name!"
                    if len(val) == 0 else True,
                    default=attribute["name"]
                ),
                description=questionary.text(
                    "What's the attribute description?",
                    validate=lambda val: "That attribute need a description!"
                    if len(val) == 0 else True,
                    default=attribute["description"]
                ),
                type=questionary.text(
                    "What's the attribute type?",
                    default=attribute["type"]
                ),
                identifier=questionary.confirm(
                    "That attribute should be consider as an identifier?",
                    default=attribute["identifier"]
                )
            ).ask()

            answers["attributes"].append(attribute)

        print("\r\nThat's all for the existing attributes.")
        create_attr = questionary.confirm(
            "Would you like to add another attribute?", default=True).ask()

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

            answers["attributes"].append(attribute)
            print("")
            create_attr = questionary.confirm(
                "Would you like to add another attribute?").ask()

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            UpdateEntity.show()

        answers["project_name"] = project_name
        answers["name"] = entity_name

        contract = UpdateEntityAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        entity = EntityView.from_contract(contract)
        print(f"The entity {entity.name} has been updated.")
        exit(0)
