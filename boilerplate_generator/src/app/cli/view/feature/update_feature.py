"""This module handle the form and show a feature from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .feature.read_feature.read_feature_adapter\
    import ReadFeatureAdapter
from boilerplate_generator.src.app.adapter\
    .feature.update_feature.update_feature_adapter\
    import UpdateFeatureAdapter

from boilerplate_generator.src.app.cli.entity_view.feature.feature_view\
    import FeatureView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class UpdateFeature:

    def show(self, wanted_project=None, wanted_feature=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        feature_name = Factory.select_feature(project_name, wanted_feature, ifr.save_path)

        if feature_name is None:
            print(f"\r\nWhoups, we found no feature in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["project_name"] = project_name
        inputs["name"] = feature_name

        contract = ReadFeatureAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        feature = FeatureView.from_contract(contract)

        answers = questionary.form(
            description=questionary.text(
                "Can you describe the feature?",
                validate=lambda val: "That feature need a description!"
                if len(val) == 0 else True,
                default=feature.description
            ),
            scenario=questionary.text(
                "Can you describe the scenario?",
                validate=lambda val: "That feature need a scenario!"
                if len(val) == 0 else True,
                default=feature.scenario
            ),
            given=questionary.text(
                "Can you describe the 'Given' of that scenario?",
                validate=lambda val: "That scenario need a Given!"
                if len(val) == 0 else True,
                default=feature.given
            ),
            when=questionary.text(
                "Can you describe the 'When' of that scenario?",
                validate=lambda val: "That scenario need a When!"
                if len(val) == 0 else True,
                default=feature.when
            ),
            then=questionary.text(
                "Can you describe the 'Then' of that scenario?",
                validate=lambda val: "That scenario need a Then!"
                if len(val) == 0 else True,
                default=feature.then
            ),
        ).ask()

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            self.show()

        answers["project_name"] = project_name
        answers["name"] = feature_name

        contract = UpdateFeatureAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        feature = FeatureView.from_contract(contract)
        print(f"The feature {feature.name} has been updated.")
        exit(0)
