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

from boilerplate_generator.src.app.adapter.\
    usecase.create_usecase.create_usecase_adapter\
    import CreateUsecaseAdapter
from boilerplate_generator.src.app.adapter.\
    usecase.read_usecase.read_usecase_adapter\
    import ReadUsecaseAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/constraints/boilerplate_generator/delete_entity_usecase.constraint",
          "Delete an entity and check if the linked usecase are deleted.")
def test_delete_entity_usecase():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have an <entity> with some CRUDL <usecases>.")
def given_delete_entity_usecase(context):
    context["project"] = Factory.create_project("DeleteUsecase")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("DeleteUsecase")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["usecase"] = Factory.create_usecase("DeleteUsecase")
    context["usecase"]["project_name"] = context["project"]["name"]
    context["usecase"]["entity_name"] = context["entity"]["name"]
    CreateUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)


@when("I use DeleteEntity.")
def when_delete_entity_usecase(context):
    entity_contract = DeleteEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["entity_contract"] = entity_contract
    usecase_contract = ReadUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)
    context["usecase_contract"] = usecase_contract


@then("The linked <usecases> are deleted too.")
def then_delete_entity_usecase(context):
    assert context["entity_contract"].\
        deleted == True
    assert context["usecase_contract"].\
        error == "This Usecase, doesn't look like to exist"
