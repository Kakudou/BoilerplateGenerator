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
from boilerplate_generator.src.app.adapter.\
    entity.update_entity.update_entity_adapter\
    import UpdateEntityAdapter

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/update_entity.feature",
          "Update a Entity.")
def test_update_entity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("i have a <entity> already created.")
def given_update_entity(context):
    context["project"] = Factory.create_project("UpdateEntityInfile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("UpdateEntityInFile")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)

@when("i use UpdateEntity with <entity_name>.")
def when_update_entity(context):
    context["entity"]["domain"] = "changed"
    output_contract = UpdateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("i see the updated information of my <entity>.")
def then_update_entity(context):
    assert context["output_contract"].\
        name == context["entity"]["name"]
    assert context["output_contract"].\
        domain == context["entity"]["domain"]
    assert context["output_contract"].\
        attributes == context["entity"]["attributes"]
    os.remove(f"{context['project']['path']}/{context['project']['name']}.yml")
