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
    entity.list_entity.list_entity_adapter\
    import ListEntityAdapter

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/list_entity.feature",
          "List all entity.")
def test_list_entity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have 3 <entity> already created.")
def given_list_entity(context):
    context["project"] = Factory.create_project("ListEntityInFile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity1"] = Factory.create_entity("ListEntity1InFile")
    context["entity1"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity1"], STORAGE_ENGINE)
    context["entity2"] = Factory.create_entity("ListEntity2InFile")
    context["entity2"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity2"], STORAGE_ENGINE)
    context["entity3"] = Factory.create_entity("ListEntity3InFile")
    context["entity3"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity3"], STORAGE_ENGINE)


@when("I use ListEntity.")
def when_list_entity(context):
    output_contract = ListEntityAdapter.execute(context["entity1"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have a list with the 3 <entity_name>.")
def then_list_entity(context):
    assert context\
        ["entity1"]["name"] in context["output_contract"].all_entitys
    assert context\
        ["entity2"]["name"] in context["output_contract"].all_entitys
    assert context\
        ["entity3"]["name"] in context["output_contract"].all_entitys
    os.remove(f"{context['project']['path']}/{context['project']['name']}.yml")
