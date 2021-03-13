import os
import pytest

from pytest_bdd\
    import scenario, given, when, then

from boilerplate_generator.tests.factory\
    import Factory

from boilerplate_generator.src.app.adapter.\
    project.create_project.create_project_adapter\
    import CreateProjectAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/create_project.feature",
          "Create a project.")
def test_create_project():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have <project_name>, <project_path> and <project_types>.")
def given_create_project(context):
    context["project"] = Factory.create_project("CreateProject")


@when("i execute CreateProject.")
def when_create_project(context):
    output_contract = CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired project created.")
def then_create_project(context):
    assert context["output_contract"].\
        name == context["project"]["name"]
    assert context["output_contract"].\
        path == context["project"]["path"]
    assert context["output_contract"].\
        types == context["project"]["types"]
