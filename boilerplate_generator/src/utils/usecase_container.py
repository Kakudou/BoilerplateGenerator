"""This module is probably one of the most important,\
    allow me to dynamically import usecase with the good storage engine"""
import os
import re

from importlib import import_module


class UsecaseContainer:
    """This class defined a usecase_container

    Functions:
    ----------
    get:
        get back the good usecase and DAO implementation

    """

    @staticmethod
    def get(usecase: str, method: str):
        """This function will make the usecase with the good DAO implementation

        Parameters:
        -----------
        usecase: str
            The name of the usecase we want
        method: str
            The name of the storage engine we want

        Returns:
        --------
        Class
            The usecase with the right dao engine

        """
        uc_snake = re.sub(r'(?!^)([A-Z]+)', r'_\1', usecase).lower()

        for a, b, c in os.walk("boilerplate_generator"
                               "/src/boilerplate_generator/usecase"):
            for file in c:
                if file == f"{uc_snake}.py":
                    module = import_module(f"{a.replace('/','.')}.{uc_snake}")
                    klass = getattr(module, usecase)

        for a, b, c in os.walk("boilerplate_generator/src/boilerplate_generator/entity"):
            if "__pycache__" not in a:
                for file in c:
                    entity_snakecase = re.split(r'\.py', file)[0]
                    if entity_snakecase in uc_snake:
                        entity_name = entity_snakecase
                        break

        klassrepo = None
        entity = ''.join(word.title() for word in entity_name.split('_'))
        for a, b, c in os.walk("boilerplate_generator/src/app/repository"):
            for file in c:
                if file == f"{entity_name}_{method.lower()}_repository.py":
                    module = import_module(f"{a.replace('/','.')}"
                                           f".{entity_name}_"
                                           f"{method.lower()}_repository")
                    klassrepo = getattr(module, f"{entity}{method}Repository")
        if klassrepo is None:
            print(f"The repository: {entity_name}_{method.lower()}_repository.py, doesn't look like to exist")
            exit(1)

        return klass(klassrepo())
