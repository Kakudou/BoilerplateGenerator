"""This module is the entrance of the cli application."""
import click
import collections

from boilerplate_generator.src\
    import VERSION

from boilerplate_generator.src.app.cli.view.project.create_project\
    import CreateProject
from boilerplate_generator.src.app.cli.view.project.read_project\
    import ReadProject
from boilerplate_generator.src.app.cli.view.project.update_project\
    import UpdateProject
from boilerplate_generator.src.app.cli.view.project.delete_project\
    import DeleteProject
from boilerplate_generator.src.app.cli.view.project.list_projects\
    import ListProjects
from boilerplate_generator.src.app.cli.view.project.generate_structure\
    import GenerateStructure

from boilerplate_generator.src.app.cli.view.feature.create_feature\
    import CreateFeature
from boilerplate_generator.src.app.cli.view.feature.read_feature\
    import ReadFeature
from boilerplate_generator.src.app.cli.view.feature.update_feature\
    import UpdateFeature
from boilerplate_generator.src.app.cli.view.feature.delete_feature\
    import DeleteFeature
from boilerplate_generator.src.app.cli.view.feature.list_features\
    import ListFeatures


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
    def ______________________projects______________________ ():
        pass

    @start.command()
    def create_project():
        """Create a project"""
        click.echo("let's create a new project")
        cp = CreateProject()
        cp.show()

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def read_project(project_name, files_dir):
        """Read a project"""
        click.echo("Let me read you that project")
        sp = ReadProject()
        sp.show(project_name, files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def update_project(project_name, files_dir):
        """Update a project"""
        click.echo("Let's update that project")
        up = UpdateProject()
        up.show(project_name, files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def delete_project(project_name, files_dir):
        """Delete a project"""
        click.echo("Let's delete a project")
        up = DeleteProject()
        up.show(project_name, files_dir)

    @start.command()
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def list_projects(files_dir):
        """List all projects"""
        click.echo("Let me show you all projects")
        lp = ListProjects()
        lp.show(files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    @click.option("--force", "force", help="Will force the generation", is_flag=True)
    def generate_structure(project_name, files_dir, force):
        """Generate structure"""
        click.echo("let's generate a project structure")
        gs = GenerateStructure()
        gs.show(project_name, files_dir, force)

    @start.command()
    def ______________________features______________________ ():
        pass

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def create_feature(project_name, files_dir):
        """Create a feature"""
        click.echo("let's create a new feature")
        cf = CreateFeature()
        cf.show(project_name, files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-f", "--feature", "feature_name", help="The name of the targeted feature")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def read_feature(project_name, feature_name, files_dir):
        """Read a feature"""
        click.echo("let's read a feature")
        rf = ReadFeature()
        rf.show(project_name, feature_name, files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-f", "--feature", "feature_name", help="The name of the targeted feature")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def update_feature(project_name, feature_name, files_dir):
        """Update a feature"""
        click.echo("let's read a feature")
        uf = UpdateFeature()
        uf.show(project_name, feature_name, files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-f", "--feature", "feature_name", help="The name of the targeted feature")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def delete_feature(project_name, feature_name, files_dir):
        """Delete a feature"""
        click.echo("let's delete a feature")
        df = DeleteFeature()
        df.show(project_name, feature_name, files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def list_features(project_name, files_dir):
        """List all features"""
        click.echo("let's list all features")
        lf = ListFeatures()
        lf.show(project_name, files_dir)
