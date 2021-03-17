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


class CreateUsecase:

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

        inputs["entity_name"] = entity_name
        print("-----")

        print("")
        inputs["type_"] = questionary.select(
            "What types of usecase this will be?",
            choices=["Create", "Read", "Update", "Delete", "List", "Custom"],
            use_pointer=True,
        ).ask()

        inputs["input_attrs"] = []
        inputs["output_attrs"] = []

        if "Custom" == inputs["type_"]:
            inputs["name"] = questionary.text(
                "What's the usecase name?",
                validate=lambda val: "That usecase need a name!"
                if len(val) == 0 else True,
            ).ask()
            inputs["description"] = questionary.text(
                "What's the usecase description?",
                validate=lambda val: "That usecase need a description!"
                if len(val) == 0 else True,
            ).ask()
            print("")
            create_attr = questionary.confirm(
                "Would you like to add an input_attr?", default=False).ask()

            while create_attr:
                input_attr = questionary.form(
                    name=questionary.text(
                        "What's the input_attr name?",
                        validate=lambda val: "That input_attr need a name!"
                        if len(val) == 0 else True,
                    ),
                    description=questionary.text(
                        "What's the input_attr description?",
                        validate=lambda val: "That input_attr need a description!"
                        if len(val) == 0 else True,
                    ),
                    type=questionary.text(
                        "What's the input_attr type?",
                        default="str"
                    ),
                    identifier=questionary.confirm(
                        "That input_attr should be consider as an identifier?",
                        default=False)
                ).ask()

                inputs["input_attrs"].append(input_attr)
                print("")
                create_attr = questionary.confirm(
                    "Would you like to add another input_attr?").ask()

            print("")
            create_attr = questionary.confirm(
                "Would you like to add an output_attr?", default=False).ask()

            while create_attr:
                output_attr = questionary.form(
                    name=questionary.text(
                        "What's the output_attr name?",
                        validate=lambda val: "That output_attr need a name!"
                        if len(val) == 0 else True,
                    ),
                    description=questionary.text(
                        "What's the output_attr description?",
                        validate=lambda val: "That output_attr need a description!"
                        if len(val) == 0 else True,
                    ),
                    type=questionary.text(
                        "What's the output_attr type?",
                        default="str"
                    ),
                    identifier=questionary.confirm(
                        "That output_attr should be consider as an identifier?",
                        default=False)
                ).ask()

                inputs["output_attrs"].append(output_attr)
                print("")
                create_attr = questionary.confirm(
                    "Would you like to add another output_attr?").ask()

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            CreateUsecase.show(wanted_project, wanted_entity, file_dir)

        contract = CreateUsecaseAdapter.execute(inputs)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        usecase = UsecaseView.from_contract(contract)
        print(f"The usecase {usecase.name} has been created.")
        exit(0)
