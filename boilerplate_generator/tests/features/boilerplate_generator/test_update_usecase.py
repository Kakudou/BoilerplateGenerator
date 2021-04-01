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
from boilerplate_generator.src.app.adapter.\
    usecase.update_usecase.update_usecase_adapter\
    import UpdateUsecaseAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/update_usecase.feature",
          "Update a Usecase.")
def test_update_usecase():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("i have a <usecase> already created.")
def given_update_usecase(context):
    context["project"] = Factory.create_project("UpdateUsecase")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("UpdateUsecase")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["usecase"] = Factory.create_usecase("UpdateUsecase")
    context["usecase"]["project_name"] = context["project"]["name"]
    context["usecase"]["entity_name"] = context["entity"]["name"]
    CreateUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)


@when("i use UpdateUsecase with <usecase_name>.")
def when_update_usecase(context):
    context["usecase"]["description"] = "changed"
    context["usecase"]["type_"] = "changed"
    output_contract = UpdateUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("i see the updated information of my <usecase>.")
def then_update_usecase(context):
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
