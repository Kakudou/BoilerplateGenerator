"""This module handle the form and show a project from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .usecase.generate_usecase.generate_usecase_adapter\
    import GenerateUsecaseAdapter
from boilerplate_generator.src.app.adapter\
    .project.read_project.read_project_adapter\
    import ReadProjectAdapter
from boilerplate_generator.src.app.cli.entity_view.project.project_view\
    import ProjectView
from boilerplate_generator.src.app.adapter\
    .usecase.read_usecase.read_usecase_adapter\
    import ReadUsecaseAdapter
from boilerplate_generator.src.app.cli.entity_view.usecase.usecase_view\
    import UsecaseView
from boilerplate_generator.src.app.adapter\
    .entity.read_entity.read_entity_adapter\
    import ReadEntityAdapter
from boilerplate_generator.src.app.cli.entity_view.entity.entity_view\
    import EntityView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class GenerateUsecase:

    @staticmethod
    def show(wanted_project=None, wanted_usecase=None, file_dir=None, force=False):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["name"] = project_name

        contract = ReadProjectAdapter.execute(inputs)
        project = ProjectView.from_contract(contract)

        usecase_name = Factory.select_usecase(project.name, wanted_usecase, ifr.save_path)

        if usecase_name is None:
            print(f"\r\nWhoups, we found no usecase in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["name"] = usecase_name
        inputs["project_name"] = project_name

        contract = ReadUsecaseAdapter.execute(inputs)
        usecase = UsecaseView.from_contract(contract)

        inputs = {}
        inputs["name"] = usecase.entity_name
        inputs["project_name"] = project_name

        contract = ReadEntityAdapter.execute(inputs)
        entity = EntityView.from_contract(contract)

        inputs = {}
        inputs["usecase_name"] = usecase_name
        inputs["entity_name"] = entity.name
        inputs["entity_domain"] = entity.domain
        inputs["entity_attributes"] = entity.attributes
        inputs["project_name"] = project.name
        inputs["project_path"] = project.path
        inputs["project_types"] = project.types
        inputs["force"] = force

        contract = GenerateUsecaseAdapter.execute(inputs)
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
