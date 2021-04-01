import os
import pytest
import shutil

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
    entity.generate_entity.generate_entity_adapter\
    import GenerateEntityAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/generate_entity.feature",
          "Generate a entity.")
def test_generate_entity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <entity>.")
def given_generate_entity(context):
    context["project"] = Factory.create_project("GenerateEntity")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("GenerateEntity")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)


@when("I execute GenerateEntity.")
def when_generate_entity(context):
    context["generate"] = {}
    context["generate"]["entity_name"] = context["entity"]["name"]
    context["generate"]["force"] = True
    context["generate"]["project_name"] = context["project"]["name"]
    context["generate"]["project_path"] = context["project"]["path"]
    context["generate"]["project_types"] = context["project"]["types"]

    output_contract = GenerateEntityAdapter.execute(context["generate"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired Entity and test generated.")
def then_generate_entity(context):
    try:
        dest_path = f"{context['project']['path']}/{context['project']['name']}"
        assert os.path.exists(f"{dest_path}/generate_entity/src/app/dto/domain_entity/generate_entity_dto.py")
        assert os.path.exists(f"{dest_path}/generate_entity/src/app/repository/inmemory/domain_entity/generate_entity_inmemory_repository.py")
        assert os.path.exists(f"{dest_path}/generate_entity/src/generate_entity/entity/domain_entity/generate_entity.py")
        assert os.path.exists(f"{dest_path}/generate_entity/src/generate_entity/gateway/domain_entity/generate_entity_gateway.py")
    finally:
        shutil.rmtree(f"{context['project']['path']}/{context['project']['name']}")
