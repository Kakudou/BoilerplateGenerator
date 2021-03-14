"""This module list all"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .project.list_project.list_project_adapter\
    import ListProjectAdapter

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class ListProjects:

    def show(self, file_dir=None):

        ifr = InFilePersist()
        if file_dir is not None:
            ifr.save_path = file_dir

        contract = ListProjectAdapter.execute({})
        all_projects = contract.all_projects
        all_projects.sort()
        print("-----")

        if contract.error is not None:
            print(f"\r\nWhoups, we got some error here: {contract.error}")
            exit(1)

        if len(all_projects) == 0:
            print(f"\r\nI can't find any project in: {file_dir}")
        else:
            print(f"\r\nI've found all of this projects in: {file_dir}")
            for project_name in all_projects:
                print(f"{project_name}")

        exit(0)
