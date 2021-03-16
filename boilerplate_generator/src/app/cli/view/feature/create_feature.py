"""This module handle the form and show a project from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .feature.create_feature.create_feature_adapter\
    import CreateFeatureAdapter
from boilerplate_generator.src.app.cli.entity_view.feature.feature_view\
    import FeatureView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class CreateFeature:

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

        inputs = questionary.form(
            name=questionary.text(
                "What's the name of the feature ?",
                validate=lambda val: "That feature need a name!"
                if len(val) == 0 else True,
            ),
            description=questionary.text(
                "Can you describe the feature?",
                validate=lambda val: "That feature need a description!"
                if len(val) == 0 else True,
            ),
            scenario=questionary.text(
                "Can you describe the scenario?",
                validate=lambda val: "That feature need a scenario!"
                if len(val) == 0 else True,
            ),
            given=questionary.text(
                "Can you describe the 'Given' of that scenario?",
                validate=lambda val: "That scenario need a Given!"
                if len(val) == 0 else True,
            ),
            when=questionary.text(
                "Can you describe the 'When' of that scenario?",
                validate=lambda val: "That scenario need a When!"
                if len(val) == 0 else True,
            ),
            then=questionary.text(
                "Can you describe the 'Then' of that scenario?",
                validate=lambda val: "That scenario need a Then!"
                if len(val) == 0 else True,
            ),
        ).ask()

        inputs["project_name"] = project_name

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            CreateFeature.show(wanted_project, file_dir)

        contract = CreateFeatureAdapter.execute(inputs)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        feature = FeatureView.from_contract(contract)
        print(f"The feature {feature.name} has been created.")

        exit(0)
