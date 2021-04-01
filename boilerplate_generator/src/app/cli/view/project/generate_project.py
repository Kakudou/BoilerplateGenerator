"""This module handle the form and show a project from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .project.read_project.read_project_adapter\
    import ReadProjectAdapter
from boilerplate_generator.src.app.cli.entity_view.project.project_view\
    import ProjectView
from boilerplate_generator.src.app.adapter\
    .usecase.read_usecase.read_usecase_adapter\
    import ReadUsecaseAdapter
from boilerplate_generator.src.app.cli.entity_view.usecase.usecase_view\
    import UsecaseView
from boilerplate_generator.src.app.adapter\
    .entity.read_entity.read_entity_adapter\
    import ReadEntityAdapter
from boilerplate_generator.src.app.cli.entity_view.entity.entity_view\
    import EntityView

from boilerplate_generator.src.app.adapter\
    .feature.list_feature.list_feature_adapter\
    import ListFeatureAdapter
from boilerplate_generator.src.app.adapter\
    .constraint.list_constraint.list_constraint_adapter\
    import ListConstraintAdapter
from boilerplate_generator.src.app.adapter\
    .entity.list_entity.list_entity_adapter\
    import ListEntityAdapter
from boilerplate_generator.src.app.adapter\
    .usecase.list_usecase.list_usecase_adapter\
    import ListUsecaseAdapter

from boilerplate_generator.src.app.adapter\
    .project.generate_structure_project.generate_structure_project_adapter\
    import GenerateStructureProjectAdapter
from boilerplate_generator.src.app.adapter\
    .feature.generate_feature.generate_feature_adapter\
    import GenerateFeatureAdapter
from boilerplate_generator.src.app.adapter\
    .constraint.generate_constraint.generate_constraint_adapter\
    import GenerateConstraintAdapter
from boilerplate_generator.src.app.adapter\
    .entity.generate_entity.generate_entity_adapter\
    import GenerateEntityAdapter
from boilerplate_generator.src.app.adapter\
    .usecase.generate_usecase.generate_usecase_adapter\
    import GenerateUsecaseAdapter

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class GenerateProject:

    @staticmethod
    def show(wanted_project=None, file_dir=None, force=False):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["name"] = project_name

        contract = ReadProjectAdapter.execute(inputs)
        project = ProjectView.from_contract(contract)

        inputs = {}
        inputs["project_name"] = project.name
        inputs["force"] = force

        contract = GenerateStructureProjectAdapter.execute(inputs)
        print("-----")
        print("Generate the Structure of the project.")

        inputs = {}
        inputs["project_name"] = project_name

        contract = ListFeatureAdapter.execute(inputs)
        all_features = contract.all_features

        for feature_name in all_features:
            inputs = {}
            inputs["feature_name"] = feature_name
            inputs["project_name"] = project.name
            inputs["project_path"] = project.path
            inputs["project_types"] = project.types
            inputs["force"] = force

            contract = GenerateFeatureAdapter.execute(inputs)
            print("-----")
            print(f"Generate the Feature: {feature_name}")

        inputs = {}
        inputs["project_name"] = project_name

        contract = ListConstraintAdapter.execute(inputs)
        all_constraints = contract.all_constraints

        for constraint_name in all_constraints:
            inputs = {}
            inputs["constraint_name"] = constraint_name
            inputs["project_name"] = project.name
            inputs["project_path"] = project.path
            inputs["project_types"] = project.types
            inputs["force"] = force

            contract = GenerateConstraintAdapter.execute(inputs)
            print("-----")
            print(f"Generate the Constraint: {constraint_name}")

        inputs = {}
        inputs["project_name"] = project_name

        contract = ListEntityAdapter.execute(inputs)
        all_entities = contract.all_entities

        for entity_name in all_entities:
            inputs = {}
            inputs["entity_name"] = entity_name
            inputs["project_name"] = project.name
            inputs["project_path"] = project.path
            inputs["project_types"] = project.types
            inputs["force"] = force

            contract = GenerateEntityAdapter.execute(inputs)
            print("-----")
            print(f"Generate the Entity: {entity_name}")

        inputs = {}
        inputs["project_name"] = project_name

        contract = ListUsecaseAdapter.execute(inputs)
        all_usecases = contract.all_usecases

        for usecase_name in all_usecases:

            inputs = {}
            inputs["name"] = usecase_name
            inputs["project_name"] = project_name

            contract = ReadUsecaseAdapter.execute(inputs)
            usecase = UsecaseView.from_contract(contract)

            inputs = {}
            inputs["name"] = usecase.entity_name
            inputs["project_name"] = project_name

            contract = ReadEntityAdapter.execute(inputs)
            entity = EntityView.from_contract(contract)

            inputs = {}
            inputs["usecase_name"] = usecase_name
            inputs["entity_name"] = entity.name
            inputs["entity_domain"] = entity.domain
            inputs["entity_attributes"] = entity.attributes
            inputs["project_name"] = project.name
            inputs["project_path"] = project.path
            inputs["project_types"] = project.types
            inputs["force"] = force

            contract = GenerateUsecaseAdapter.execute(inputs)
            print("-----")
            print(f"Generate the Usecase: {usecase_name}")
