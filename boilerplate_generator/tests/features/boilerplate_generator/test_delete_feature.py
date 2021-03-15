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
    feature.delete_feature.delete_feature_adapter\
    import DeleteFeatureAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/delete_feature.feature",
          "Delete a Feature.")
def test_create_feature():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <feature> already created.")
def given_delete_feature(context):
    context["project"] = Factory.create_project("DeleteFeature")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["feature"] = Factory.create_feature("DeleteFeature")
    context["feature"]["project_name"] = context["project"]["name"]
    CreateFeatureAdapter.execute(context["feature"], STORAGE_ENGINE)


@when("I use DeleteFeature with <feature_name>.")
def when_delete_feature(context):
    output_contract = DeleteFeatureAdapter.execute(context["feature"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("The <feature> was removed.")
def then_delete_feature(context):
    assert context["output_contract"].\
        deleted == True
