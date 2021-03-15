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


class Factory:

    @classmethod
    def select_project(cls, wanted_project, save_path):

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

    @classmethod
    def select_feature(cls, project_name, wanted_feature, save_path):

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
