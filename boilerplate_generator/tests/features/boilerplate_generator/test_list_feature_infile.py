import os
import pytest

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
    feature.list_feature.list_feature_adapter\
    import ListFeatureAdapter

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/list_feature.feature",
          "List all feature.")
def test_list_feature():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have 3 <feature> already created.")
def given_list_feature(context):
    context["project"] = Factory.create_project("ListFeatureInFile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["feature1"] = Factory.create_feature("ListFeature1InFile")
    context["feature1"]["project_name"] = context["project"]["name"]
    CreateFeatureAdapter.execute(context["feature1"], STORAGE_ENGINE)
    context["feature2"] = Factory.create_feature("ListFeature2InFile")
    context["feature2"]["project_name"] = context["project"]["name"]
    CreateFeatureAdapter.execute(context["feature2"], STORAGE_ENGINE)
    context["feature3"] = Factory.create_feature("ListFeature3InFile")
    context["feature3"]["project_name"] = context["project"]["name"]
    CreateFeatureAdapter.execute(context["feature3"], STORAGE_ENGINE)


@when("I use ListFeature.")
def when_list_feature(context):
    output_contract = ListFeatureAdapter.execute(context["feature1"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have a list with the 3 <feature_name>.")
def then_list_feature(context):
    assert context\
        ["feature1"]["name"] in context["output_contract"].all_features
    assert context\
        ["feature2"]["name"] in context["output_contract"].all_features
    assert context\
        ["feature3"]["name"] in context["output_contract"].all_features
    os.remove(f"{context['project']['path']}/{context['project']['name']}.yml")
