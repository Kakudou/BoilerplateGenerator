"""This module handle the form and show a usecase from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .usecase.read_usecase.read_usecase_adapter\
    import ReadUsecaseAdapter
from boilerplate_generator.src.app.adapter\
    .usecase.update_usecase.update_usecase_adapter\
    import UpdateUsecaseAdapter

from boilerplate_generator.src.app.cli.entity_view.usecase.usecase_view\
    import UsecaseView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class UpdateUsecase:

    @staticmethod
    def show(wanted_project=None, wanted_usecase=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        usecase_name = Factory.select_usecase(project_name, wanted_usecase, ifr.save_path)

        if usecase_name is None:
            print(f"\r\nWhoups, we found no usecase in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["project_name"] = project_name
        inputs["name"] = usecase_name

        contract = ReadUsecaseAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        usecase = UsecaseView.from_contract(contract)

        print("")
        answers = {}

        if "Custom" == usecase.type_:
            answers["description"] = questionary.text(
                "What's the usecase description?",
                validate=lambda val: "That usecase need a description!"
                if len(val) == 0 else True,
                default=usecase.description
            ).ask()
            print("")

            print("\r\nLet see the existing input_attrs.")
            answers["input_attrs"] = []
            for attribute in usecase.input_attrs:
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

                answers["input_attrs"].append(attribute)

            print("\r\nThat's all for the existing input_attrs.")
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

                answers["input_attrs"].append(attribute)
                print("")
                create_attr = questionary.confirm(
                    "Would you like to add another attribute?").ask()

            print("\r\nLet see the existing output_attrs.")
            answers["output_attrs"] = []
            for attribute in usecase.output_attrs:
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

                answers["output_attrs"].append(attribute)

            print("\r\nThat's all for the existing output_attrs.")
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

                answers["output_attrs"].append(attribute)
                print("")
                create_attr = questionary.confirm(
                    "Would you like to add another attribute?").ask()
        else:
            print("Only the update for Custom usecase are allowed.")
            exit(1)

        answers["project_name"] = project_name
        answers["entity_name"] = usecase.entity_name
        answers["name"] = usecase_name
        answers["type_"] = usecase.type_

        contract = UpdateUsecaseAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        usecase = UsecaseView.from_contract(contract)
        print(f"The usecase {usecase.name} has been updated.")
        exit(0)
