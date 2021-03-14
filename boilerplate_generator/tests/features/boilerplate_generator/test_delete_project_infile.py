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
    project.delete_project.delete_project_adapter\
    import DeleteProjectAdapter

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/delete_project.feature",
          "Delete a Project.")
def test_delete_project():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <project> already created.")
def given_delete_project(context):
    context["project"] = Factory.create_project("DeleteProjectInFile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)


@when("I use DeleteProject with <project_name>.")
def when_delete_project(context):
    output_contract = DeleteProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("The <project> was removed.")
def then_delete_project(context):
    assert context["output_contract"].\
        deleted == True
