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
from boilerplate_generator.src.app.adapter.\
    constraint.delete_constraint.delete_constraint_adapter\
    import DeleteConstraintAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/delete_constraint.feature",
          "Delete a Constraint.")
def test_create_constraint():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <constraint> already created.")
def given_delete_constraint(context):
    context["project"] = Factory.create_project("DeleteConstraint")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["constraint"] = Factory.create_constraint("DeleteConstraint")
    context["constraint"]["project_name"] = context["project"]["name"]
    CreateConstraintAdapter.execute(context["constraint"], STORAGE_ENGINE)


@when("I use DeleteConstraint with <constraint_name>.")
def when_delete_constraint(context):
    output_contract = DeleteConstraintAdapter.execute(context["constraint"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("The <constraint> was removed.")
def then_delete_constraint(context):
    assert context["output_contract"].\
        deleted == True
