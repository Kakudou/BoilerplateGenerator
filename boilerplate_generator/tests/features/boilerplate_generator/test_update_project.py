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
    project.update_project.update_project_adapter\
    import UpdateProjectAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/update_project.feature",
          "Update a Project.")
def test_update_project():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("i have a <project> already created.")
def given_update_project(context):
    context["project"] = Factory.create_project("UpdateProject")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)


@when("i use UpdateProject with <project_name>.")
def when_update_project(context):
    context["project"]["path"] = "~/"
    context["project"]["types"] = ["cli"]
    output_contract = UpdateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("i see the updated information of my <project>.")
def then_update_project(context):
    assert context["output_contract"].\
        name == context["project"]["name"]
    assert context["output_contract"].\
        path == context["project"]["path"] == "~/"
    assert context["output_contract"].\
        types == context["project"]["types"] == ["cli"]
