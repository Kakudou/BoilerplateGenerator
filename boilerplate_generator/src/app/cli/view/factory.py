from sys import exit

import questionary
from questionary\
    import Separator

from math\
    import ceil

from boilerplate_generator.src.app.adapter\
    .project.list_project.list_project_adapter\
    import ListProjectAdapter
from boilerplate_generator.src.app.adapter\
    .feature.list_feature.list_feature_adapter\
    import ListFeatureAdapter
from boilerplate_generator.src.app.adapter\
    .constraint.list_constraint.list_constraint_adapter\
    import ListConstraintAdapter
from boilerplate_generator.src.app.adapter\
    .entity.list_entity.list_entity_adapter\
    import ListEntityAdapter
from boilerplate_generator.src.app.adapter\
    .usecase.list_usecase.list_usecase_adapter\
    import ListUsecaseAdapter


class Factory:

    @staticmethod
    def select_project(wanted_project, save_path):

        project_name = None

        contract = ListProjectAdapter.execute({})
        all_projects = contract.all_projects
        all_projects.sort()
        if wanted_project is None or wanted_project not in all_projects:
            if len(all_projects) == 0:
                print(f"\r\nNo project found in: {save_path}")
                exit(1)

            min_elmnt = 0
            max_elmnt = len(all_projects)
            paginate = 5

            actual_page = 0
            first_elmnt = min_elmnt
            last_elemnt = paginate if max_elmnt >= paginate else max_elmnt

            number_page = int(ceil(max_elmnt / paginate) - 1)

            project_name = "Get next projects"
            while ("Get next projects" in project_name) \
                    or ("Get previous projects" in project_name):

                choices = []
                choices.append("Get previous projects")
                choices.append("Get next projects")

                choices.append(Separator('-= The Projects =-'))
                choices.extend(all_projects[first_elmnt:last_elemnt])
                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-'))

                project_name = questionary.select(
                    "Select one project in all of that:",
                    choices=choices,
                    use_pointer=True,
                    use_shortcuts=True,
                    use_arrow_keys=True,).ask()

                if "Get next projects" in project_name:
                    actual_page = actual_page + 1 \
                        if actual_page + 1 < number_page else number_page
                elif "Get previous projects" in project_name:
                    actual_page = actual_page - 1 \
                        if actual_page - 1 > 0 else 0

                first_elmnt = 5 * actual_page
                last_elemnt = (5 * actual_page + paginate) \
                    if (5 * actual_page + paginate) <= max_elmnt else max_elmnt
        else:
            project_name = wanted_project

        return project_name

    @staticmethod
    def select_feature(project_name, wanted_feature, save_path):

        feature_name = None

        contract = ListFeatureAdapter.execute({"project_name": project_name})
        all_features = contract.all_features
        all_features.sort()
        if wanted_feature is None or wanted_feature not in all_features:
            if len(all_features) == 0:
                print(f"\r\nNo feature found in: {save_path}")
                exit(1)

            min_elmnt = 0
            max_elmnt = len(all_features)
            paginate = 5

            actual_page = 0
            first_elmnt = min_elmnt
            last_elemnt = paginate if max_elmnt >= paginate else max_elmnt

            number_page = int(ceil(max_elmnt / paginate) - 1)

            feature_name = "Get next features"
            while ("Get next features" in feature_name) \
                    or ("Get previous features" in feature_name):

                choices = []
                choices.append("Get previous features")
                choices.append("Get next features")

                choices.append(Separator('-= The Features =-'))
                choices.extend(all_features[first_elmnt:last_elemnt])
                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-'))

                feature_name = questionary.select(
                    "Select one feature in all of that:",
                    choices=choices,
                    use_pointer=True,
                    use_shortcuts=True,
                    use_arrow_keys=True,).ask()

                if "Get next features" in feature_name:
                    actual_page = actual_page + 1 \
                        if actual_page + 1 < number_page else number_page
                elif "Get previous features" in feature_name:
                    actual_page = actual_page - 1 \
                        if actual_page - 1 > 0 else 0

                first_elmnt = 5 * actual_page
                last_elemnt = (5 * actual_page + paginate) \
                    if (5 * actual_page + paginate) <= max_elmnt else max_elmnt
        else:
            feature_name = wanted_feature

        return feature_name

    @staticmethod
    def select_constraint(project_name, wanted_constraint, save_path):

        constraint_name = None

        contract = ListConstraintAdapter.execute({"project_name": project_name})
        all_constraints = contract.all_constraints
        all_constraints.sort()
        if wanted_constraint is None or wanted_constraint not in all_constraints:
            if len(all_constraints) == 0:
                print(f"\r\nNo constraint found in: {save_path}")
                exit(1)

            min_elmnt = 0
            max_elmnt = len(all_constraints)
            paginate = 5

            actual_page = 0
            first_elmnt = min_elmnt
            last_elemnt = paginate if max_elmnt >= paginate else max_elmnt

            number_page = int(ceil(max_elmnt / paginate) - 1)

            constraint_name = "Get next constraints"
            while ("Get next constraints" in constraint_name) \
                    or ("Get previous constraints" in constraint_name):

                choices = []
                choices.append("Get previous constraints")
                choices.append("Get next constraints")

                choices.append(Separator('-= The Constraints =-'))
                choices.extend(all_constraints[first_elmnt:last_elemnt])
                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-'))

                constraint_name = questionary.select(
                    "Select one constraint in all of that:",
                    choices=choices,
                    use_pointer=True,
                    use_shortcuts=True,
                    use_arrow_keys=True,).ask()

                if "Get next constraints" in constraint_name:
                    actual_page = actual_page + 1 \
                        if actual_page + 1 < number_page else number_page
                elif "Get previous constraints" in constraint_name:
                    actual_page = actual_page - 1 \
                        if actual_page - 1 > 0 else 0

                first_elmnt = 5 * actual_page
                last_elemnt = (5 * actual_page + paginate) \
                    if (5 * actual_page + paginate) <= max_elmnt else max_elmnt
        else:
            constraint_name = wanted_constraint

        return constraint_name

    @staticmethod
    def select_entity(project_name, wanted_entity, save_path):

        entity_name = None

        contract = ListEntityAdapter.execute({"project_name": project_name})
        all_entitys = contract.all_entitys
        all_entitys.sort()
        if wanted_entity is None or wanted_entity not in all_entitys:
            if len(all_entitys) == 0:
                print(f"\r\nNo entity found in: {save_path}")
                exit(1)

            min_elmnt = 0
            max_elmnt = len(all_entitys)
            paginate = 5

            actual_page = 0
            first_elmnt = min_elmnt
            last_elemnt = paginate if max_elmnt >= paginate else max_elmnt

            number_page = int(ceil(max_elmnt / paginate) - 1)

            entity_name = "Get next entitys"
            while ("Get next entitys" in entity_name) \
                    or ("Get previous entitys" in entity_name):

                choices = []
                choices.append("Get previous entitys")
                choices.append("Get next entitys")

                choices.append(Separator('-= The Entitys =-'))
                choices.extend(all_entitys[first_elmnt:last_elemnt])
                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-'))

                entity_name = questionary.select(
                    "Select one entity in all of that:",
                    choices=choices,
                    use_pointer=True,
                    use_shortcuts=True,
                    use_arrow_keys=True,).ask()

                if "Get next entitys" in entity_name:
                    actual_page = actual_page + 1 \
                        if actual_page + 1 < number_page else number_page
                elif "Get previous entitys" in entity_name:
                    actual_page = actual_page - 1 \
                        if actual_page - 1 > 0 else 0

                first_elmnt = 5 * actual_page
                last_elemnt = (5 * actual_page + paginate) \
                    if (5 * actual_page + paginate) <= max_elmnt else max_elmnt
        else:
            entity_name = wanted_entity

        return entity_name

    @staticmethod
    def select_usecase(project_name, wanted_usecase, save_path):

        usecase_name = None

        contract = ListUsecaseAdapter.execute({"project_name": project_name})
        all_usecases = contract.all_usecases
        all_usecases.sort()
        if wanted_usecase is None or wanted_usecase not in all_usecases:
            if len(all_usecases) == 0:
                print(f"\r\nNo usecase found in: {save_path}")
                exit(1)

            min_elmnt = 0
            max_elmnt = len(all_usecases)
            paginate = 5

            actual_page = 0
            first_elmnt = min_elmnt
            last_elemnt = paginate if max_elmnt >= paginate else max_elmnt

            number_page = int(ceil(max_elmnt / paginate) - 1)

            usecase_name = "Get next usecases"
            while ("Get next usecases" in usecase_name) \
                    or ("Get previous usecases" in usecase_name):

                choices = []
                choices.append("Get previous usecases")
                choices.append("Get next usecases")

                choices.append(Separator('-= The Usecases =-'))
                choices.extend(all_usecases[first_elmnt:last_elemnt])
                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-'))

                usecase_name = questionary.select(
                    "Select one usecase in all of that:",
                    choices=choices,
                    use_pointer=True,
                    use_shortcuts=True,
                    use_arrow_keys=True,).ask()

                if "Get next usecases" in usecase_name:
                    actual_page = actual_page + 1 \
                        if actual_page + 1 < number_page else number_page
                elif "Get previous usecases" in usecase_name:
                    actual_page = actual_page - 1 \
                        if actual_page - 1 > 0 else 0

                first_elmnt = 5 * actual_page
                last_elemnt = (5 * actual_page + paginate) \
                    if (5 * actual_page + paginate) <= max_elmnt else max_elmnt
        else:
            usecase_name = wanted_usecase

        return usecase_name
