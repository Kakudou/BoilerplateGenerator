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
    project.list_project.list_project_adapter\
    import ListProjectAdapter

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/list_project.feature",
          "List all project.")
def test_list_project():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have 3 <project> already created.")
def given_list_project(context):
    context["project1"] = Factory.create_project("ListProject1InFile")
    CreateProjectAdapter.execute(context["project1"], STORAGE_ENGINE)
    context["project2"] = Factory.create_project("ListProject2InFile")
    CreateProjectAdapter.execute(context["project2"], STORAGE_ENGINE)
    context["project3"] = Factory.create_project("ListProject3InFile")
    CreateProjectAdapter.execute(context["project3"], STORAGE_ENGINE)


@when("I use ListProject.")
def when_list_project(context):
    output_contract = ListProjectAdapter.execute({}, STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have a list with the 3 <project_name>.")
def then_list_project(context):
    assert context\
        ["project1"]["name"] in context["output_contract"].all_projects
    assert context\
        ["project2"]["name"] in context["output_contract"].all_projects
    assert context\
        ["project3"]["name"] in context["output_contract"].all_projects
    os.remove(f"{context['project1']['path']}/{context['project1']['name']}.yml")
    os.remove(f"{context['project2']['path']}/{context['project2']['name']}.yml")
    os.remove(f"{context['project3']['path']}/{context['project3']['name']}.yml")
