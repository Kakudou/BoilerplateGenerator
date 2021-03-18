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
    project.generate_structure_project.generate_structure_project_adapter\
    import GenerateStructureProjectAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/generate_structure_project.feature",
          "Generate the project structure.")
def test_generate_structure():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <project>.")
def given_generate_structure(context):
    context["project"] = Factory.create_project("GenerateStructure")
    project = CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)


@when("I execute GenerateStructure with <project_name>.")
def when_generate_structure(context):
    context["project_name"] = context["project"]["name"]
    context["force"] = False

    output_contract = GenerateStructureProjectAdapter.execute(context,
                                                              STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the structure of the project generated.")
def then_generate_entity(context):
    try:
        dest_path = f"{context['project']['path']}/{context['project']['name']}"

        assert os.path.exists(f"{dest_path}")
        assert os.path.exists(f"{dest_path}/generate_structure")
        assert os.path.exists(f"{dest_path}/generate_structure/constraints")
        assert os.path.exists(f"{dest_path}/generate_structure/constraints/generate_structure")
        assert os.path.exists(f"{dest_path}/generate_structure/features")
        assert os.path.exists(f"{dest_path}/generate_structure/features/generate_structure")
        assert os.path.exists(f"{dest_path}/generate_structure/src")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/adapter")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/dto")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/repository")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/repository/inmemory")
        assert os.path.exists(f"{dest_path}/generate_structure/src/generate_structure")
        assert os.path.exists(f"{dest_path}/generate_structure/src/generate_structure/entity")
        assert os.path.exists(f"{dest_path}/generate_structure/src/generate_structure/gateway")
        assert os.path.exists(f"{dest_path}/generate_structure/src/generate_structure/usecase")
        assert os.path.exists(f"{dest_path}/generate_structure/src/utils")
        assert os.path.exists(f"{dest_path}/generate_structure/tests")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/constraints")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/constraints/generate_structure")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/features")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/features/generate_structure")
        assert os.path.exists(f"{dest_path}/generate_structure/constraints/cli")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/constraints/cli")
        assert os.path.exists(f"{dest_path}/generate_structure/features/cli")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/features/cli")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/cli")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/cli/entity_view")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/cli/view")
        assert os.path.exists(f"{dest_path}/generate_structure/constraints/web")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/constraints/web")
        assert os.path.exists(f"{dest_path}/generate_structure/features/web")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/features/web")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/web")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/web/entity_view")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/web/view")
        assert os.path.exists(f"{dest_path}/generate_structure/constraints/api")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/constraints/api")
        assert os.path.exists(f"{dest_path}/generate_structure/features/api")
        assert os.path.exists(f"{dest_path}/generate_structure/tests/features/api")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/api")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/api/entity_view")
        assert os.path.exists(f"{dest_path}/generate_structure/src/app/api/view")
        assert os.path.isfile(f"{dest_path}/.gitignore")
        assert os.path.isfile(f"{dest_path}/LICENSE")
        assert os.path.isfile(f"{dest_path}/README.md")
        assert os.path.isfile(f"{dest_path}/requirements")
        assert os.path.isfile(f"{dest_path}/setup.py")
        assert os.path.isfile(f"{dest_path}/generate_structure/src/__init__.py")
        assert os.path.isfile(f"{dest_path}/generate_structure/src/app/repository/inmemory/inmemory_persist.py")
        assert os.path.isfile(f"{dest_path}/generate_structure/src/generate_structure/gateway/abstract_gateway.py")
        assert os.path.isfile(f"{dest_path}/generate_structure/src/utils/debug.py")
        assert os.path.isfile(f"{dest_path}/generate_structure/src/utils/singleton.py")
        assert os.path.isfile(f"{dest_path}/generate_structure/src/utils/usecase_container.py")
    finally:
        shutil.rmtree(f"{context['project']['path']}/{context['project']['name']}")
