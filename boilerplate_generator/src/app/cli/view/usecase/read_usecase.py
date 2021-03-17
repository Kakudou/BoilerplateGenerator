"""This module handle the form and show a usecase from it"""
from sys import\
    exit

from boilerplate_generator.src.app.adapter\
    .usecase.read_usecase.read_usecase_adapter\
    import ReadUsecaseAdapter

from boilerplate_generator.src.app.cli.entity_view.usecase.usecase_view\
    import UsecaseView

from boilerplate_generator.src.app.cli.view.factory\
    import Factory

from boilerplate_generator.src.app.repository.infile.infile_persist\
    import InFilePersist


class ReadUsecase:

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
        print(f"\r\nThe usecase 'name' is: {usecase.name}")
        print(f"The usecase 'description' is: {usecase.description}")
        print(f"The usecase 'type_' is: {usecase.type_}")
        if len(usecase.input_attrs) > 0:
            print("\r\nThe usecase 'input_attrs' are:")
            for attr in usecase.input_attrs:
                print(f"\r\nAttribute name: {attr['name']}")
                print(f"Attribute description: {attr['description']}")
                print(f"Attribute type: {attr['type']}")
                print(f"Attribute identifier flag: {attr['identifier']}")
        if len(usecase.output_attrs) > 0:
            print("\r\nThe usecase 'output_attrs' are:")
            for attr in usecase.output_attrs:
                print(f"\r\nAttribute name: {attr['name']}")
                print(f"Attribute description: {attr['description']}")
                print(f"Attribute type: {attr['type']}")
                print(f"Attribute identifier flag: {attr['identifier']}")

        exit(0)
