from sys import exit

from boilerplate_generator.src.app.cli.view.launch_cli\
    import LaunchCLI


def boilerplate_generator():
    """The main routine"""
    app = LaunchCLI()
    app.start()


if __name__ == "__main__":
    exit(boilerplate_generator())
