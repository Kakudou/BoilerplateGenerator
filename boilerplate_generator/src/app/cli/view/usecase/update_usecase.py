"""This module handle the form and show a usecase from it"""
from sys import\
    exit

import questionary

from boilerplate_generator.src.app.adapter\
    .usecase.read_usecase.read_usecase_adapter\
    import ReadUsecaseAdapter
from boilerplate_generator.src.app.adapter\
    .usecase.update_usecase.update_usecase_adapter\
    import UpdateUsecaseAdapter

from boilerplate_generator.src.app.cli.entity_view.usecase.usecase_view\
    import UsecaseView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class UpdateUsecase:

    @staticmethod
    def show(wanted_project=None, wanted_usecase=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        usecase_name = Factory.select_usecase(project_name, wanted_usecase, ifr.save_path)

        if usecase_name is None:
            print(f"\r\nWhoups, we found no usecase in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["project_name"] = project_name
        inputs["name"] = usecase_name

        contract = ReadUsecaseAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        usecase = UsecaseView.from_contract(contract)

        print("")
        answers = {}

        answers = Factory.create_usecase_form(usecase)

        print("")
        confirm = questionary.confirm("Are you sure of the above inputs?",
                                      default=True).ask()

        if not confirm:
            print("\r\n Ok, let's try again")
            UpdateUsecase.show()

        answers["project_name"] = project_name
        answers["entity_name"] = usecase.entity_name
        answers["name"] = usecase_name
        answers["type_"] = usecase.type_

        contract = UpdateUsecaseAdapter.execute(answers)

        if contract.error is not None:
            print(f"Whoups, we got some error here: {contract.error}")
            exit(1)

        usecase = UsecaseView.from_contract(contract)
        print(f"The usecase {usecase.name} has been updated.")
        exit(0)
