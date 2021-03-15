"""This module handle the form and show a feature from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .feature.delete_feature.delete_feature_adapter\
    import DeleteFeatureAdapter

from boilerplate_generator.src.app.cli.entity_view.feature.feature_view\
    import FeatureView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class DeleteFeature:

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

        contract = DeleteFeatureAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        if contract.deleted:
            print(f"The feature {feature_name} has been deleted.")

        exit(0)
