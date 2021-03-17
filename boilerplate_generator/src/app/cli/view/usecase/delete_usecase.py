"""This module handle the form and show a usecase from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .usecase.delete_usecase.delete_usecase_adapter\
    import DeleteUsecaseAdapter

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class DeleteUsecase:

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

        contract = DeleteUsecaseAdapter.execute(inputs)
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        if contract.deleted:
            print(f"The usecase {usecase_name} has been deleted.")

        exit(0)
