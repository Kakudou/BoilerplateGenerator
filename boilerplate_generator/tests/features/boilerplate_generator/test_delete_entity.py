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
    entity.delete_entity.delete_entity_adapter\
    import DeleteEntityAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/delete_entity.feature",
          "Delete a Entity.")
def test_create_entity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <entity> already created.")
def given_delete_entity(context):
    context["project"] = Factory.create_project("DeleteEntity")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("DeleteEntity")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)


@when("I use DeleteEntity with <entity_name>.")
def when_delete_entity(context):
    output_contract = DeleteEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("The <entity> was removed.")
def then_delete_entity(context):
    assert context["output_contract"].\
        deleted == True
