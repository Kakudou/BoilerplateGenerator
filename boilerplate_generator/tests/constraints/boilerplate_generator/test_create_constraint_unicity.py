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
    constraint.create_constraint.create_constraint_adapter\
    import CreateConstraintAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/constraints/boilerplate_generator/create_constraint_unicity.constraint",
          "Create a Constraint who already exist to check the error.")
def test_create_constraint_unicity():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <constraint> already created.")
def given_create_constraint_unicity(context):
    context["project"] = Factory.create_project("CreateConstraintUnicity")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["constraint"] = Factory.create_constraint("CreateConstraintUnicity")
    context["constraint"]["project_name"] = context["project"]["name"]
    CreateConstraintAdapter.execute(context["constraint"], STORAGE_ENGINE)


@when("I try to create another <constraint> with the same <constraint_name>.")
def when_create_constraint_unicity(context):
    context["constraint_double"] = Factory.create_constraint("CreateConstraintUnicity")
    context["constraint_double"]["project_name"] = context["project"]["name"]
    output_contract = CreateConstraintAdapter.execute(context["constraint_double"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have an error telling me <constraint_name> already exist.")
def then_create_constraint_unicity(context):
    assert context["output_contract"].\
        error == "The Constraint you want, already exist"
