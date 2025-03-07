"""This module is the entrance of the cli application."""
from boilerplate_generator.src.app.cli.view import *


class OrderedGroup(click.Group):
    def __init__(self, name=None, commands=None, **attrs):
        super(OrderedGroup, self).__init__(name, commands, **attrs)
        #: the registered subcommands by their exported names.
        self.commands = commands or collections.OrderedDict()

    def list_commands(self, ctx):
        return self.commands


class LaunchCLI:
    CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

    @click.group(help=f"CLI tool to manage the boilerplate of projects, version {VERSION}", cls=OrderedGroup, context_settings=CONTEXT_SETTINGS)
    def start():
        pass

    @start.command()
    def ______________________projects______________________():
        pass

    @start.command(short_help="Create a Project.")
    def create_project():
        """Create a project"""
        click.echo("let's create a new project")
        CreateProject.show()

    @start.command(short_help="Read a Project.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def read_project(project_name, files_dir):
        """Read a project"""
        click.echo("Let me read you that project")
        ReadProject.show(project_name, files_dir)

    @start.command(short_help="Update a Project.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def update_project(project_name, files_dir):
        """Update a project"""
        click.echo("Let's update that project")
        UpdateProject.show(project_name, files_dir)

    @start.command(short_help="Delete a Project.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def delete_project(project_name, files_dir):
        """Delete a project"""
        click.echo("Let's delete a project")
        DeleteProject.show(project_name, files_dir)

    @start.command(short_help="List all Projects")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def list_projects(files_dir):
        """List all projects"""
        click.echo("Let me show you all projects")
        ListProjects.show(files_dir)

    @start.command()
    def ______________________features______________________():
        pass

    @start.command(short_help="Create a Feature.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def create_feature(project_name, files_dir):
        """Create a feature"""
        click.echo("let's create a new feature")
        CreateFeature.show(project_name, files_dir)

    @start.command(short_help="Read a Feature.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-f", "--feature", "feature_name", help="The name of the targeted feature")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def read_feature(project_name, feature_name, files_dir):
        """Read a feature"""
        click.echo("let's read a feature")
        ReadFeature.show(project_name, feature_name, files_dir)

    @start.command(short_help="Update a Feature.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-f", "--feature", "feature_name", help="The name of the targeted feature")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def update_feature(project_name, feature_name, files_dir):
        """Update a feature"""
        click.echo("let's read a feature")
        UpdateFeature.show(project_name, feature_name, files_dir)

    @start.command(short_help="Delete a Feature.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-f", "--feature", "feature_name", help="The name of the targeted feature")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def delete_feature(project_name, feature_name, files_dir):
        """Delete a feature"""
        click.echo("let's delete a feature")
        DeleteFeature.show(project_name, feature_name, files_dir)

    @start.command(short_help="List all Features.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def list_features(project_name, files_dir):
        """List all features"""
        click.echo("let's list all features")
        ListFeatures.show(project_name, files_dir)

    @start.command()
    def ______________________constraints______________________():
        pass

    @start.command(short_help="Create a Constraint.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def create_constraint(project_name, files_dir):
        """Create a constraint"""
        click.echo("let's create a new constraint")
        CreateConstraint.show(project_name, files_dir)

    @start.command(short_help="Read a Constraint.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-c", "--constraint", "constraint_name", help="The name of the targeted constraint")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def read_constraint(project_name, constraint_name, files_dir):
        """Read a constraint"""
        click.echo("let's read a constraint")
        ReadConstraint.show(project_name, constraint_name, files_dir)

    @start.command(short_help="Update a Constraint.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-c", "--constraint", "constraint_name", help="The name of the targeted constraint")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def update_constraint(project_name, constraint_name, files_dir):
        """Update a constraint"""
        click.echo("let's read a constraint")
        UpdateConstraint.show(project_name, constraint_name, files_dir)

    @start.command(short_help="Delete a Constraint.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-c", "--constraint", "constraint_name", help="The name of the targeted constraint")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def delete_constraint(project_name, constraint_name, files_dir):
        """Delete a constraint"""
        click.echo("let's delete a constraint")
        DeleteConstraint.show(project_name, constraint_name, files_dir)

    @start.command(short_help="List all Constraints.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def list_constraints(project_name, files_dir):
        """List all constraints"""
        click.echo("let's list all constraints")
        ListConstraints.show(project_name, files_dir)

    @start.command()
    def ______________________entities______________________():
        pass

    @start.command(short_help="Create a Entity.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def create_entity(project_name, files_dir):
        """Create a entity"""
        click.echo("let's create a new entity")
        CreateEntity.show(project_name, files_dir)

    @start.command(short_help="Read a Entity.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-e", "--entity", "entity_name", help="The name of the targeted entity")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def read_entity(project_name, entity_name, files_dir):
        """Read a entity"""
        click.echo("let's read a entity")
        ReadEntity.show(project_name, entity_name, files_dir)

    @start.command(short_help="Update a Entity.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-e", "--entity", "entity_name", help="The name of the targeted entity")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def update_entity(project_name, entity_name, files_dir):
        """Update a entity"""
        click.echo("let's read a entity")
        UpdateEntity.show(project_name, entity_name, files_dir)

    @start.command(short_help="Delete a Entity.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-e", "--entity", "entity_name", help="The name of the targeted entity")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def delete_entity(project_name, entity_name, files_dir):
        """Delete a entity"""
        click.echo("let's delete a entity")
        DeleteEntity.show(project_name, entity_name, files_dir)

    @start.command(short_help="List all Entities.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def list_entities(project_name, files_dir):
        """List all entities"""
        click.echo("let's list all entities")
        ListEntities.show(project_name, files_dir)

    @start.command()
    def ______________________usecases______________________():
        pass

    @start.command(short_help="Create CRUDL for an Entity.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-e", "--entity", "entity_name", help="The name of the targeted entity")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def create_crudl(project_name, entity_name, files_dir):
        """Create a crudl"""
        click.echo("let's create a full CRUDL")
        CreateCrudl.show(project_name, entity_name, files_dir)

    @start.command(short_help="Create a Usecase.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-e", "--entity", "entity_name", help="The name of the targeted entity")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def create_usecase(project_name, entity_name, files_dir):
        """Create a usecase"""
        click.echo("let's create a new usecase")
        CreateUsecase.show(project_name, entity_name, files_dir)

    @start.command(short_help="Read a Usecase.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-u", "--usecase", "usecase_name", help="The name of the targeted usecase")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def read_usecase(project_name, usecase_name, files_dir):
        """Read a usecase"""
        click.echo("let's read a usecase")
        ReadUsecase.show(project_name, usecase_name, files_dir)

    @start.command(short_help="Update a Usecase.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-u", "--usecase", "usecase_name", help="The name of the targeted usecase")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def update_usecase(project_name, usecase_name, files_dir):
        """Update a usecase"""
        click.echo("let's read a usecase")
        UpdateUsecase.show(project_name, usecase_name, files_dir)

    @start.command(short_help="Delete a Usecase.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-u", "--usecase", "usecase_name", help="The name of the targeted usecase")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def delete_usecase(project_name, usecase_name, files_dir):
        """Delete a usecase"""
        click.echo("let's delete a usecase")
        DeleteUsecase.show(project_name, usecase_name, files_dir)

    @start.command(short_help="List all Usecases.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def list_usecases(project_name, files_dir):
        """List all usecases"""
        click.echo("let's list all entities")
        ListUsecases.show(project_name, files_dir)

    @start.command()
    def ______________________generate______________________():
        pass

    @start.command(short_help="Generate the structure of a Project.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    @click.option("--force", "force", help="Will force the generation", is_flag=True)
    def generate_structure(project_name, files_dir, force):
        """Generate structure"""
        click.echo("let's generate a project structure")
        GenerateStructure.show(project_name, files_dir, force)

    @start.command(short_help="Generate a feature.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-f", "--feature", "feature_name", help="The name of the targeted feature")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    @click.option("--force", "force", help="Will force the generation", is_flag=True)
    def generate_feature(project_name, feature_name, files_dir, force):
        """Generate feature"""
        click.echo("let's generate a feature")
        GenerateFeature.show(project_name, feature_name, files_dir, force)

    @start.command(short_help="Generate a constraint.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-c", "--constraint", "constraint_name", help="The name of the targeted constraint")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    @click.option("--force", "force", help="Will force the generation", is_flag=True)
    def generate_constraint(project_name, constraint_name, files_dir, force):
        """Generate constraint"""
        click.echo("let's generate a constraint")
        GenerateConstraint.show(project_name, constraint_name, files_dir, force)

    @start.command(short_help="Generate an entity.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-e", "--entity", "entity_name", help="The name of the targeted entity")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    @click.option("--force", "force", help="Will force the generation", is_flag=True)
    def generate_entity(project_name, entity_name, files_dir, force):
        """Generate entity"""
        click.echo("let's generate an entity")
        GenerateEntity.show(project_name, entity_name, files_dir, force)

    @start.command(short_help="Generate the crudl.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-e", "--entity", "entity_name", help="The name of the targeted entity")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    @click.option("--force", "force", help="Will force the generation", is_flag=True)
    def generate_crudl(project_name, entity_name, files_dir, force):
        """Generate crudl"""
        click.echo("let's generate the CRUDL")
        GenerateCrudl.show(project_name, entity_name, files_dir, force)

    @start.command(short_help="Generate a usecase.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-u", "--usecase", "usecase_name", help="The name of the targeted usecase")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    @click.option("--force", "force", help="Will force the generation", is_flag=True)
    def generate_usecase(project_name, usecase_name, files_dir, force):
        """Generate usecase"""
        click.echo("let's generate a usecase")
        GenerateUsecase.show(project_name, usecase_name, files_dir, force)

    @start.command(short_help="Generate everything, the whole Project.")
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    @click.option("--force", "force", help="Will force the generation", is_flag=True)
    def generate_project(project_name, files_dir, force):
        """Generate everything"""
        click.echo("let's generate a everything")
        GenerateProject.show(project_name, files_dir, force)

    @start.command()
    def ______________________usage______________________():
        pass

    @start.command(short_help="Common Usage.")
    def usage():
        click.echo("""
This tool will generate the boilerplate for a Clean Architecture, with Behavior Driven Development.

The most common workflow will be:
    create-project:
        Will be used to generate the project.yml file and identify the type of project.
    create-feature:
        Will be used to create the feature for the project.
    create-constraint:
        Will be used to create the constraint for the previous feature.
    create-entity:
        Will be used to create the entity involved in the previous feature.
    create-crudl:
        Will be used to create the CRUDL usecases for the previous entity.
    create-usecase:
        Will be used to create custom usecase involving the previous entity.
    generate-project:
        Will be used to generate the whole project.

If you want more informations on the architecture behind, or to really understand what will be generated and how to use it.
Please refer to the README.md.
        """)
