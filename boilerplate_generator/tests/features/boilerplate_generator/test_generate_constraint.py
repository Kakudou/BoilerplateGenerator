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
    constraint.create_constraint.create_constraint_adapter\
    import CreateConstraintAdapter

from boilerplate_generator.src.app.adapter.\
    constraint.generate_constraint.generate_constraint_adapter\
    import GenerateConstraintAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/generate_constraint.feature",
          "Generate a constraint.")
def test_generate_constraint():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <constraint>.")
def given_generate_constraint(context):
    context["project"] = Factory.create_project("GenerateConstraint")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["constraint"] = Factory.create_constraint("GenerateConstraint")
    context["constraint"]["project_name"] = context["project"]["name"]
    CreateConstraintAdapter.execute(context["constraint"], STORAGE_ENGINE)


@when("I execute GenerateConstraint.")
def when_generate_constraint(context):
    context["generate"] = {}
    context["generate"]["constraint_name"] = context["constraint"]["name"]
    context["generate"]["force"] = True
    context["generate"]["project_name"] = context["project"]["name"]
    context["generate"]["project_path"] = context["project"]["path"]
    context["generate"]["project_types"] = context["project"]["types"]

    output_contract = GenerateConstraintAdapter.execute(context["generate"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired Constraint and test generated.")
def then_generate_constraint(context):
    try:
        dest_path = f"{context['project']['path']}/{context['project']['name']}"
        assert os.path.exists(f"{dest_path}/generate_constraint/constraints/cli/generate_constraint.constraint")
        assert os.path.exists(f"{dest_path}/generate_constraint/tests/constraints/cli/test_generate_constraint.py")
    finally:
        shutil.rmtree(f"{context['project']['path']}/{context['project']['name']}")
