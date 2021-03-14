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
    project.read_project.read_project_adapter\
    import ReadProjectAdapter

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/read_project.feature",
          "Read a Project.")
def test_read_project():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("i have a <project> already created.")
def given_read_project(context):
    context["project"] = Factory.create_project("ReadProjectInFile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)


@when("i use ReadProject with <project_name>.")
def when_read_project(context):
    output_contract = ReadProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("i see the information of my <project>.")
def then_read_project(context):
    assert context["output_contract"].\
        name == context["project"]["name"]
    assert context["output_contract"].\
        path == context["project"]["path"]
    assert context["output_contract"].\
        types == context["project"]["types"]
    os.remove(f"{context['project']['path']}/{context['project']['name']}.yml")
