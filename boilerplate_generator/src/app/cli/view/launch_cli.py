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
    def create_project():
        """Create a new project."""
        click.echo("let's create a new project")
        cp = CreateProject()
        cp.show()

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def read_project(project_name, files_dir):
        """Read a project."""
        click.echo("Let me read you that project")
        sp = ReadProject()
        sp.show(project_name, files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def update_project(project_name, files_dir):
        """Update a project."""
        click.echo("Let's update that project")
        up = UpdateProject()
        up.show(project_name, files_dir)

    @start.command()
    @click.option("-p", "--project", "project_name", help="The name of the targeted project")
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def delete_project(project_name, files_dir):
        """Delete a project."""
        click.echo("Let's delete a project")
        up = DeleteProject()
        up.show(project_name, files_dir)

    @start.command()
    @click.option("-d", "--dir", "files_dir", help="The dir of the yaml files")
    def list_projects(files_dir):
        """List all projects."""
        click.echo("Let me show you all projects")
        lp = ListProjects()
        lp.show(files_dir)
