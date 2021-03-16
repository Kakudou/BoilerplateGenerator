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
    feature.update_feature.update_feature_adapter\
    import UpdateFeatureAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/update_feature.feature",
          "Update a Feature.")
def test_update_feature():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("i have a <feature> already created.")
def given_update_feature(context):
    context["project"] = Factory.create_project("UpdateFeature")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["feature"] = Factory.create_feature("UpdateFeature")
    context["feature"]["project_name"] = context["project"]["name"]
    CreateFeatureAdapter.execute(context["feature"], STORAGE_ENGINE)

@when("i use UpdateFeature with <feature_name>.")
def when_update_feature(context):
    context["feature"]["given"] = "changed"
    context["feature"]["when"] = "changed"
    context["feature"]["then"] = "changed"
    output_contract = UpdateFeatureAdapter.execute(context["feature"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("i see the updated information of my <feature>.")
def then_update_feature(context):
    assert context["output_contract"].\
        name == context["feature"]["name"]
    assert context["output_contract"].\
        description == context["feature"]["description"]
    assert context["output_contract"].\
        scenario == context["feature"]["scenario"]
    assert context["output_contract"].\
        given == context["feature"]["given"]
    assert context["output_contract"].\
        when == context["feature"]["when"]
    assert context["output_contract"].\
        then == context["feature"]["then"]
