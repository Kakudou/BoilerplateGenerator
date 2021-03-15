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

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/constraints/boilerplate_generator/create_feature_unicity.constraint",
          "Create a Feature who already exist to check the error.")
def test_create_feature_unicity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <feature> already created.")
def given_create_feature_unicity(context):
    context["project"] = Factory.create_project("CreateFeatureUnicity")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["feature"] = Factory.create_feature("CreateFeatureUnicity")
    context["feature"]["project_name"] = context["project"]["name"]
    CreateFeatureAdapter.execute(context["feature"], STORAGE_ENGINE)


@when("I try to create another <feature> with the same <feature_name>.")
def when_create_feature_unicity(context):
    context["feature_double"] = Factory.create_feature("CreateFeatureUnicity")
    context["feature_double"]["project_name"] = context["project"]["name"]
    output_contract = CreateFeatureAdapter.execute(context["feature_double"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have an error telling me <feature_name> already exist.")
def then_create_feature_unicity(context):
    assert context["output_contract"].\
        error == "The Feature you want, already exist"
