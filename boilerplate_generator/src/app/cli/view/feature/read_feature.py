"""This module handle the form and show a feature from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .feature.read_feature.read_feature_adapter\
    import ReadFeatureAdapter

from boilerplate_generator.src.app.cli.entity_view.feature.feature_view\
    import FeatureView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class ReadFeature:

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
        print(f"\r\nThe feature 'Name' is: {feature.name}")
        print(f"The feature 'Type' is: {feature.type_}")
        print(f"The feature 'Domain' is: {feature.domain}")
        print(f"The feature 'Description' is: {feature.description}")
        print(f"The feature 'Scenario' is: {feature.scenario}")
        print(f"The feature 'Given' is: {feature.given}")
        print(f"The feature 'When' is: {feature.when}")
        print(f"The feature 'Then' is: {feature.then}")

        exit(0)
