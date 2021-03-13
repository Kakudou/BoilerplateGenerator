"""This module is the entrance of the cli application."""
import click
import collections

from boilerplate_generator.src\
    import VERSION

from boilerplate_generator.src.app.cli.view.project.create_project\
    import CreateProject


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

