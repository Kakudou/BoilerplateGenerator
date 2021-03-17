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
    usecase.delete_usecase.delete_usecase_adapter\
    import DeleteUsecaseAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/delete_usecase.feature",
          "Delete a Usecase.")
def test_create_usecase():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <usecase> already created.")
def given_delete_usecase(context):
    context["project"] = Factory.create_project("DeleteUsecase")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("DeleteUsecase")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["usecase"] = Factory.create_usecase("DeleteUsecase")
    context["usecase"]["project_name"] = context["project"]["name"]
    context["usecase"]["entity_name"] = context["entity"]["name"]
    CreateUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)


@when("I use DeleteUsecase with <usecase_name>.")
def when_delete_usecase(context):
    output_contract = DeleteUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("The <usecase> was removed.")
def then_delete_usecase(context):
    assert context["output_contract"].\
        deleted == True
