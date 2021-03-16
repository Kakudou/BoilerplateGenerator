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
    entity.create_entity.create_entity_adapter\
    import CreateEntityAdapter

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/create_entity.feature",
          "Create a entity.")
def test_create_entity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <entity_name>, <entity_domain>, <attributes> and a <project>.")
def given_create_entity(context):
    context["project"] = Factory.create_project("CreateEntityInFile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("CreateEntityInFile")
    context["entity"]["project_name"] = context["project"]["name"]


@when("I execute CreateEntity.")
def when_create_entity(context):
    output_contract = CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired Entity created.")
def then_create_entity(context):
    assert context["output_contract"].\
        name == context["entity"]["name"]
    assert context["output_contract"].\
        domain == context["entity"]["domain"]
    assert context["output_contract"].\
        attributes == context["entity"]["attributes"]
    os.remove(f"{context['project']['path']}/{context['project']['name']}.yml")
