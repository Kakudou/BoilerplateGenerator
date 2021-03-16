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
    constraint.list_constraint.list_constraint_adapter\
    import ListConstraintAdapter

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/list_constraint.feature",
          "List all constraint.")
def test_list_constraint():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have 3 <constraint> already created.")
def given_list_constraint(context):
    context["project"] = Factory.create_project("ListConstraintInFile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["constraint1"] = Factory.create_constraint("ListConstraint1InFile")
    context["constraint1"]["project_name"] = context["project"]["name"]
    CreateConstraintAdapter.execute(context["constraint1"], STORAGE_ENGINE)
    context["constraint2"] = Factory.create_constraint("ListConstraint2InFile")
    context["constraint2"]["project_name"] = context["project"]["name"]
    CreateConstraintAdapter.execute(context["constraint2"], STORAGE_ENGINE)
    context["constraint3"] = Factory.create_constraint("ListConstraint3InFile")
    context["constraint3"]["project_name"] = context["project"]["name"]
    CreateConstraintAdapter.execute(context["constraint3"], STORAGE_ENGINE)


@when("I use ListConstraint.")
def when_list_constraint(context):
    output_contract = ListConstraintAdapter.execute(context["constraint1"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have a list with the 3 <constraint_name>.")
def then_list_constraint(context):
    assert context\
        ["constraint1"]["name"] in context["output_contract"].all_constraints
    assert context\
        ["constraint2"]["name"] in context["output_contract"].all_constraints
    assert context\
        ["constraint3"]["name"] in context["output_contract"].all_constraints
    os.remove(f"{context['project']['path']}/{context['project']['name']}.yml")
