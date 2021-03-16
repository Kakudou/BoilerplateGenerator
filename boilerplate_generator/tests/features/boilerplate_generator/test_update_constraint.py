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
    constraint.update_constraint.update_constraint_adapter\
    import UpdateConstraintAdapter

STORAGE_ENGINE = "INMEMORY"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/update_constraint.feature",
          "Update a Constraint.")
def test_update_constraint():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("i have a <constraint> already created.")
def given_update_constraint(context):
    context["project"] = Factory.create_project("UpdateConstraint")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["constraint"] = Factory.create_constraint("UpdateConstraint")
    context["constraint"]["project_name"] = context["project"]["name"]
    CreateConstraintAdapter.execute(context["constraint"], STORAGE_ENGINE)

@when("i use UpdateConstraint with <constraint_name>.")
def when_update_constraint(context):
    context["constraint"]["given"] = "changed"
    context["constraint"]["when"] = "changed"
    context["constraint"]["then"] = "changed"
    output_contract = UpdateConstraintAdapter.execute(context["constraint"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("i see the updated information of my <constraint>.")
def then_update_constraint(context):
    assert context["output_contract"].\
        name == context["constraint"]["name"]
    assert context["output_contract"].\
        description == context["constraint"]["description"]
    assert context["output_contract"].\
        scenario == context["constraint"]["scenario"]
    assert context["output_contract"].\
        given == context["constraint"]["given"]
    assert context["output_contract"].\
        when == context["constraint"]["when"]
    assert context["output_contract"].\
        then == context["constraint"]["then"]
