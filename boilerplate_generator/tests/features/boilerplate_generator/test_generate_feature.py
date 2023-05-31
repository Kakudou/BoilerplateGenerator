import os
import pytest
import shutil

from pytest_bdd\
    import scenario, given, when, then

from boilerplate_generator.tests.factory\
    import Factory

from boilerplate_generator.src.app.adapter.\
    project.create_project.create_project_adapter\
    import CreateProjectAdapter
from boilerplate_generator.src.app.adapter.\
    feature.create_feature.create_feature_adapter\
    import CreateFeatureAdapter

from boilerplate_generator.src.app.adapter.\
    feature.generate_feature.generate_feature_adapter\
    import GenerateFeatureAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/generate_feature.feature",
          "Generate a feature.")
def test_generate_feature():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <feature>.")
def given_generate_feature(context):
    context["project"] = Factory.create_project("GenerateFeature")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["feature"] = Factory.create_feature("GenerateFeature")
    context["feature"]["project_name"] = context["project"]["name"]
    CreateFeatureAdapter.execute(context["feature"], STORAGE_ENGINE)


@when("I execute GenerateFeature.")
def when_generate_feature(context):
    context["generate"] = {}
    context["generate"]["feature_name"] = context["feature"]["name"]
    context["generate"]["force"] = True
    context["generate"]["project_name"] = context["project"]["name"]
    context["generate"]["project_path"] = context["project"]["path"]
    context["generate"]["project_types"] = context["project"]["types"]

    output_contract = GenerateFeatureAdapter.execute(context["generate"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired Feature and test generated.")
def then_generate_feature(context):
    try:
        dest_path = f"{context['project']['path']}/{context['project']['name']}"
        assert os.path.exists(f"{dest_path}/generate_feature/features/cli/generate_feature.feature")
        assert os.path.exists(f"{dest_path}/generate_feature/tests/a_features/cli/test_generate_feature.py")
    finally:
        shutil.rmtree(f"{context['project']['path']}/{context['project']['name']}")
