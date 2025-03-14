"""This module handle the form and show a feature from it"""
from sys import\
    exit

import re

import questionary

from boilerplate_generator.src.app.adapter\
    .project.read_project.read_project_adapter\
    import ReadProjectAdapter
from boilerplate_generator.src.app.cli.entity_view.project.project_view\
    import ProjectView

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

    @staticmethod
    def show(wanted_project=None, wanted_feature=None, file_dir=None):

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

        project_inputs = {}
        project_inputs["name"] = project_name

        contract = ReadProjectAdapter.execute(project_inputs)
        project = ProjectView.from_contract(contract)

        answers = Factory.create_feature_form(feature, project.types)

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            UpdateFeature.show()

        answers["project_name"] = project_name
        answers["name"] = feature_name
        answers["domain"] = feature_domain
        if answers["type_"] == "core":
            snakename = re.sub(r'(?!^)([A-Z]+)', r'_\1', project_name).lower()
            answers["type_"] = snakename

        contract = UpdateFeatureAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        feature = FeatureView.from_contract(contract)
        print(f"The feature {feature.name} has been updated.")
        exit(0)
