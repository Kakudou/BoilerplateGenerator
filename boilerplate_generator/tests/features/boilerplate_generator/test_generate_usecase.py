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
    usecase.create_usecase.create_usecase_adapter\
    import CreateUsecaseAdapter

from boilerplate_generator.src.app.adapter.\
    usecase.generate_usecase.generate_usecase_adapter\
    import GenerateUsecaseAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/generate_usecase.feature",
          "Generate a usecase.")
def test_generate_usecase():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <usecase>.")
def given_generate_usecase(context):
    context["project"] = Factory.create_project("GenerateUsecase")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["entity"] = Factory.create_entity("GenerateUsecase")
    context["entity"]["project_name"] = context["project"]["name"]
    CreateEntityAdapter.execute(context["entity"], STORAGE_ENGINE)
    context["usecase"] = Factory.create_usecase("GenerateUsecase")
    context["usecase"]["project_name"] = context["project"]["name"]
    context["usecase"]["entity_name"] = context["entity"]["name"]
    CreateUsecaseAdapter.execute(context["usecase"], STORAGE_ENGINE)


@when("I execute GenerateUsecase.")
def when_generate_usecase(context):
    context["generate"] = {}
    context["generate"]["usecase_name"] = context["usecase"]["name"]
    context["generate"]["force"] = True
    context["generate"]["entity_name"] = context["entity"]["name"]
    context["generate"]["entity_domain"] = context["entity"]["domain"]
    context["generate"]["entity_attributes"] = context["entity"]["attributes"]
    context["generate"]["project_name"] = context["project"]["name"]
    context["generate"]["project_path"] = context["project"]["path"]
    context["generate"]["project_types"] = context["project"]["types"]

    output_contract = GenerateUsecaseAdapter.execute(context["generate"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired Usecase and test generated.")
def then_generate_usecase(context):
    try:
        dest_path = f"{context['project']['path']}/{context['project']['name']}"
        assert os.path.exists(f"{dest_path}/generate_usecase/src/app/adapter/domain_entity/generate_usecase/generate_usecase_adapter.py")
        assert os.path.exists(f"{dest_path}/generate_usecase/src/generate_usecase/usecase/domain_entity/generate_usecase/generate_usecase.py")
        assert os.path.exists(f"{dest_path}/generate_usecase/src/generate_usecase/usecase/domain_entity/generate_usecase/generate_usecase_inputport.py")
        assert os.path.exists(f"{dest_path}/generate_usecase/src/generate_usecase/usecase/domain_entity/generate_usecase/generate_usecase_inputport_builder.py")
        assert os.path.exists(f"{dest_path}/generate_usecase/src/generate_usecase/usecase/domain_entity/generate_usecase/generate_usecase_outputport.py")
        assert os.path.exists(f"{dest_path}/generate_usecase/src/generate_usecase/usecase/domain_entity/generate_usecase/generate_usecase_outputport_builder.py")
    finally:
        shutil.rmtree(f"{context['project']['path']}/{context['project']['name']}")
