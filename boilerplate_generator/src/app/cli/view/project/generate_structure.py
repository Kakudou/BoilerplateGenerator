"""This module handle the form and show a project from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .project.generate_structure_project.generate_structure_project_adapter\
    import GenerateStructureProjectAdapter

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class GenerateStructure:

    @staticmethod
    def show(wanted_project=None, file_dir=None, force=False):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["project_name"] = project_name
        inputs["force"] = force

        contract = GenerateStructureProjectAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        if len(contract.folders) > 0:
            print("\r\nThe following folders have been created:")
            for folder in contract.folders:
                print(f"{folder}")
        else:
            print("No folders have been created")

        if len(contract.files) > 0:
            print("\r\nThe following files have been created:")
            for file in contract.files:
                print(f"{file}")
        else:
            print("No files have been created")

        exit(0)
