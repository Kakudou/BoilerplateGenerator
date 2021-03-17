"""This module handle the form and show a usecase from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .usecase.list_usecase.list_usecase_adapter\
    import ListUsecaseAdapter

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class ListUsecases:

    @staticmethod
    def show(wanted_project=None, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        project_name = Factory.select_project(wanted_project, ifr.save_path)

        if project_name is None:
            print(f"\r\nWhoups, we found no project in: {ifr.save_path}.")
            exit(1)

        inputs = {}
        inputs["project_name"] = project_name

        contract = ListUsecaseAdapter.execute(inputs)
        all_usecases = contract.all_usecases
        all_usecases.sort()
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        if len(all_usecases) == 0:
            print(f"\r\nI can't find any usecase in: {ifr.save_path}/{project_name}")
        else:
            print(f"\r\nI've found all of this usecases in: {ifr.save_path}/{project_name}")
            for usecase_name in all_usecases:
                print(f"{usecase_name}")

        exit(0)
