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
          "/features/boilerplate_generator/create_usecase.feature",
          "Create a usecase.")
def test_create_usecase():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <usecase> with <name>, <description>, <type_>, <input_atts>, <output_attrs>, a <entity> and a <project>.")
def given_create_usecase(context):
    context["project"] = Factory.create_project("CreateUsecase")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("CreateUsecase")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["usecase"] = Factory.create_usecase("CreateUsecase")
    context["usecase"]["project_name"] = context["project"]["name"]
    context["usecase"]["entity_name"] = context["entity"]["name"]


@when("I execute CreateUsecase.")
def when_create_usecase(context):
    output_contract = CreateUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired Usecase created.")
def then_create_usecase(context):
    assert context["output_contract"].\
        name == context["usecase"]["name"]
    assert context["output_contract"].\
        description == context["usecase"]["description"]
    assert context["output_contract"].\
        type_ == context["usecase"]["type_"]
    assert context["output_contract"].\
        input_attrs == context["usecase"]["input_attrs"]
    assert context["output_contract"].\
        output_attrs == context["usecase"]["output_attrs"]
