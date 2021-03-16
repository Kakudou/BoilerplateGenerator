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

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/constraints/boilerplate_generator/create_entity_unicity.constraint",
          "Create a Entity who already exist to check the error.")
def test_create_entity_unicity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <entity> already created.")
def given_create_entity_unicity(context):
    context["project"] = Factory.create_project("CreateEntityUnicity")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("CreateEntityUnicity")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)


@when("I try to create another <entity> with the same <entity_name>.")
def when_create_entity_unicity(context):
    context["entity_double"] = Factory.create_entity("CreateEntityUnicity")
    context["entity_double"]["project_name"] = context["project"]["name"]
    output_contract = CreateEntityAdapter.execute(context["entity_double"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have an error telling me <entity_name> already exist.")
def then_create_entity_unicity(context):
    assert context["output_contract"].\
        error == "The Entity you want, already exist"
