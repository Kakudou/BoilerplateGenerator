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
    usecase.create_usecase.create_usecase_adapter\
    import CreateUsecaseAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/constraints/boilerplate_generator/create_usecase_unicity.constraint",
          "Create a Usecase who already exist to check the error.")
def test_create_usecase_unicity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <usecase> already created.")
def given_create_usecase_unicity(context):
    context["project"] = Factory.create_project("CreateUsecaseUnicity")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("CreateUsecaseUnicity")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["usecase"] = Factory.create_usecase("CreateUsecaseUnicity")
    context["usecase"]["project_name"] = context["project"]["name"]
    context["usecase"]["entity_name"] = context["entity"]["name"]
    CreateUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)


@when("I try to create another <usecase> with the same <usecase_name>.")
def when_create_usecase_unicity(context):
    context["usecase_double"] = Factory.create_usecase("CreateUsecaseUnicity")
    context["usecase_double"]["project_name"] = context["project"]["name"]
    context["usecase_double"]["entity_name"] = context["entity"]["name"]
    output_contract = CreateUsecaseAdapter.execute(context["usecase_double"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have an error telling me <usecase_name> already exist.")
def then_create_usecase_unicity(context):
    assert context["output_contract"].\
        error == "The Usecase you want, already exist"
