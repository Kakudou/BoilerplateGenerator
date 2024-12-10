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

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/create_feature.feature",
          "Create a feature.")
def test_create_feature():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <feature> with <scenario>, <given>, <when>, <then> and a <project>.")
def given_create_feature(context):
    context["project"] = Factory.create_project("CreateFeatureInFile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["feature"] = Factory.create_feature("CreateFeatureInFile")
    context["feature"]["project_name"] = context["project"]["name"]


@when("I execute CreateFeature.")
def when_create_feature(context):
    output_contract = CreateFeatureAdapter.execute(context["feature"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired Feature created.")
def then_create_feature(context):
    assert context["output_contract"].\
        name == context["feature"]["name"]
    assert context["output_contract"].\
        description == context["feature"]["description"]
    assert context["output_contract"].\
        domain == context["feature"]["domain"]
    assert context["output_contract"].\
        scenario == context["feature"]["scenario"]
    assert context["output_contract"].\
        given == context["feature"]["given"]
    assert context["output_contract"].\
        when == context["feature"]["when"]
    assert context["output_contract"].\
        then == context["feature"]["then"]
    os.remove(f"{context['project']['path']}/{context['project']['name']}.yml")
