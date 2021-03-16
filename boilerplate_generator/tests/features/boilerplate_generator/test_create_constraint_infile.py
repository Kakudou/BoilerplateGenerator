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

STORAGE_ENGINE = "INFILE"
__fullpath = os.path.dirname(os.path.abspath(__file__))


@scenario(f"{__fullpath.split('/BoilerplateGenerator/')[0]}"
          "/BoilerplateGenerator/boilerplate_generator"
          "/features/boilerplate_generator/create_constraint.feature",
          "Create a constraint.")
def test_create_constraint():
    pass


@pytest.fixture(scope="function")
def context():
    return {}


@given("I have a <constraint> with <scenario>, <given>, <when>, <then> and a <project>.")
def given_create_constraint(context):
    context["project"] = Factory.create_project("CreateConstraintInFile")
    CreateProjectAdapter.execute(context["project"], STORAGE_ENGINE)
    context["constraint"] = Factory.create_constraint("CreateConstraintInFile")
    context["constraint"]["project_name"] = context["project"]["name"]


@when("I execute CreateConstraint.")
def when_create_constraint(context):
    output_contract = CreateConstraintAdapter.execute(context["constraint"], STORAGE_ENGINE)
    context["output_contract"] = output_contract


@then("I have the desired Constraint created.")
def then_create_constraint(context):
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
    os.remove(f"{context['project']['path']}/{context['project']['name']}.yml")
