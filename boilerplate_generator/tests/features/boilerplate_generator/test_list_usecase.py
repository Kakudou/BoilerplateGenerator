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
    usecase.list_usecase.list_usecase_adapter\
    import ListUsecaseAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/list_usecase.feature",
          "List all usecase.")
def test_list_usecase():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have 3 <usecase> already created.")
def given_list_usecase(context):
    context["project"] = Factory.create_project("ListUsecase")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("ListUsecase")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["usecase1"] = Factory.create_usecase("ListUsecase1")
    context["usecase1"]["project_name"] = context["project"]["name"]
    context["usecase1"]["entity_name"] = context["entity"]["name"]
    CreateUsecaseAdapter.execute(context["usecase1"], STORAGE_ENGINE)
    context["usecase2"] = Factory.create_usecase("ListUsecase2")
    context["usecase2"]["project_name"] = context["project"]["name"]
    context["usecase2"]["entity_name"] = context["entity"]["name"]
    CreateUsecaseAdapter.execute(context["usecase2"], STORAGE_ENGINE)
    context["usecase3"] = Factory.create_usecase("ListUsecase3")
    context["usecase3"]["project_name"] = context["project"]["name"]
    context["usecase3"]["entity_name"] = context["entity"]["name"]
    CreateUsecaseAdapter.execute(context["usecase3"], STORAGE_ENGINE)


@when("I use ListUsecase.")
def when_list_usecase(context):
    output_contract = ListUsecaseAdapter.execute(context["usecase1"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have a list with the 3 <usecase_name>.")
def then_list_usecase(context):
    assert context\
        ["usecase1"]["name"] in context["output_contract"].all_usecases
    assert context\
        ["usecase2"]["name"] in context["output_contract"].all_usecases
    assert context\
        ["usecase3"]["name"] in context["output_contract"].all_usecases
