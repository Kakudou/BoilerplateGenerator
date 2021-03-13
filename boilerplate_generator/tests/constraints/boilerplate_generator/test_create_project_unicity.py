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
          "/BoilerplateGenerator/boilerplate_generator/constraints"
          "/boilerplate_generator/create_project_unicity.constraint",
          "Create a Project who already exist to check the error.")
def test_create_project_unicity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("i have a <project> already created.")
def given_create_project_unicity(context):
    context["project_origin"] = Factory.create_project("CreateProjectUnicity")
    CreateProjectAdapter.execute(context["project_origin"], STORAGE_ENGINE)


@when("i try to create another <project> with the same <project_name>.")
def when_create_project_unicity(context):
    context["project_double"] = Factory.create_project("CreateProjectUnicity")
    output_contract = CreateProjectAdapter.execute(context["project_double"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("i have an error telling me <project_name> already exist.")
def then_create_project_unicity(context):
    assert context["output_contract"].\
        error == "The Project you want, already exist"
