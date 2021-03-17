from sys import exit

import questionary
from questionary\
    import Separator, Choice
from prompt_toolkit.shortcuts\
    import CompleteStyle

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
                if number_page > 0:
                    if actual_page > 0:
                        choices.append("Get previous projects")
                    if actual_page != number_page:
                        choices.append("Get next projects")

                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-\n'))
                choices.append(Separator('-= The Projects =-\n'))
                choices.extend(all_projects[first_elmnt:last_elemnt])

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
                choices = []
                if number_page > 0:
                    if actual_page > 0:
                        choices.append("Get previous features")
                    if actual_page != number_page:
                        choices.append("Get next features")

                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-\n'))
                choices.append(Separator('-= The Features =-\n'))
                choices.extend(all_features[first_elmnt:last_elemnt])

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
                if number_page > 0:
                    if actual_page > 0:
                        choices.append("Get previous constraints")
                    if actual_page != number_page:
                        choices.append("Get next constraints")

                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-\n'))
                choices.append(Separator('-= The Constraints =-\n'))
                choices.extend(all_constraints[first_elmnt:last_elemnt])

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
                if number_page > 0:
                    if actual_page > 0:
                        choices.append("Get previous entitys")
                    if actual_page != number_page:
                        choices.append("Get next entitys")

                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-\n'))
                choices.append(Separator('-= The Entitys =-\n'))
                choices.extend(all_entitys[first_elmnt:last_elemnt])

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
                if number_page > 0:
                    if actual_page > 0:
                        choices.append("Get previous usecases")
                    if actual_page != number_page:
                        choices.append("Get next usecases")

                if number_page > 0:
                    choices.append(Separator(
                        f'-= Pages {actual_page+1}/{number_page+1} =-\n'))
                choices.append(Separator('-= The Usecases =-\n'))
                choices.extend(all_usecases[first_elmnt:last_elemnt])

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

    @staticmethod
    def create_project_form(project_update=None):

        project = {}

        if project_update is None:
            project["name"] = questionary.text(
                "What's the project name?",
                validate=lambda val: "That project need a name!"
                if len(val) == 0 else True,
            ).ask()

        project["path"] = questionary.path(
            "What's the path for this project?",
            complete_style=CompleteStyle.MULTI_COLUMN,
            validate=lambda val: "That project need to be somewhere!"
            if len(val) == 0 else True,
            only_directories=True,
            default=project_update.path
            if project_update is not None else "",
        ).ask()

        choices = ["web", "cli", "api"]
        if project_update is not None:
            for choice in project_update.types:
                choices.remove(choice)
                choices.append(Choice(choice, checked=True))

            choices.reverse()
        project["types"] = questionary.checkbox(
            "What types of project this will be?",
            choices=choices,
            use_pointer=True,
        ).ask()

        return project

    @staticmethod
    def create_feature_form(feature_update=None):
        feature = {}

        if feature_update is None:
            feature["name"] = questionary.text(
                "What's the name of the feature ?",
                validate=lambda val: "That feature need a name!"
                if len(val) == 0 else True,
            ).ask()
        feature["description"] = questionary.text(
            "Can you describe the feature?",
            validate=lambda val: "That feature need a description!"
            if len(val) == 0 else True,
            default=feature_update.description
            if feature_update is not None else ""
        ).ask()
        feature["scenario"] = questionary.text(
            "Can you describe the scenario?",
            validate=lambda val: "That feature need a scenario!"
            if len(val) == 0 else True,
            default=feature_update.scenario
            if feature_update is not None else ""
        ).ask()
        feature["given"] = questionary.text(
            "Can you describe the 'Given' of that scenario?",
            validate=lambda val: "That scenario need a Given!"
            if len(val) == 0 else True,
            default=feature_update.given
            if feature_update is not None else ""
        ).ask()
        feature["when"] = questionary.text(
            "Can you describe the 'When' of that scenario?",
            validate=lambda val: "That scenario need a When!"
            if len(val) == 0 else True,
            default=feature_update.when
            if feature_update is not None else ""
        ).ask()
        feature["then"] = questionary.text(
            "Can you describe the 'Then' of that scenario?",
            validate=lambda val: "That scenario need a Then!"
            if len(val) == 0 else True,
            default=feature_update.then
            if feature_update is not None else ""
        ).ask()

        return feature

    @staticmethod
    def create_constraint_form(constraint_update=None):
        constraint = {}

        if constraint_update is None:
            constraint["name"] = questionary.text(
                "What's the name of the constraint ?",
                validate=lambda val: "That constraint need a name!"
                if len(val) == 0 else True,
            ).ask()
        constraint["description"] = questionary.text(
            "Can you describe the constraint?",
            validate=lambda val: "That constraint need a description!"
            if len(val) == 0 else True,
            default=constraint_update.description
            if constraint_update is not None else ""
        ).ask()
        constraint["scenario"] = questionary.text(
            "Can you describe the scenario?",
            validate=lambda val: "That constraint need a scenario!"
            if len(val) == 0 else True,
            default=constraint_update.scenario
            if constraint_update is not None else ""
        ).ask()
        constraint["given"] = questionary.text(
            "Can you describe the 'Given' of that scenario?",
            validate=lambda val: "That scenario need a Given!"
            if len(val) == 0 else True,
            default=constraint_update.given
            if constraint_update is not None else ""
        ).ask()
        constraint["when"] = questionary.text(
            "Can you describe the 'When' of that scenario?",
            validate=lambda val: "That scenario need a When!"
            if len(val) == 0 else True,
            default=constraint_update.when
            if constraint_update is not None else ""
        ).ask()
        constraint["then"] = questionary.text(
            "Can you describe the 'Then' of that scenario?",
            validate=lambda val: "That scenario need a Then!"
            if len(val) == 0 else True,
            default=constraint_update.then
            if constraint_update is not None else ""
        ).ask()

        return constraint

    @staticmethod
    def create_entity_form(entity_update=None):
        entity = {}

        if entity_update is None:
            entity["name"] = questionary.text(
                "What's the entity name?",
                validate=lambda val: "That entity need a name!"
                if len(val) == 0 else True,
            ).ask()

        entity["domain"] = questionary.text(
            "What's the entity domain?",
            validate=lambda val: "That domain need a name!"
            if len(val) == 0 else True,
            default=entity["name"]
            if entity_update is None else entity_update.domain
        ).ask()

        attrs = None
        if entity_update is not None:
            attrs = entity_update.attributes
        print("")
        entity["attributes"] = Factory._create_attributes_form(attrs)

        return entity

    @staticmethod
    def _create_attributes_form(attrs_update=None):
        attrs = []

        if attrs_update is not None and len(attrs_update) > 0:
            print("Let see the existing attributes.")

            for attribute in attrs_update:
                print("")
                attribute = questionary.form(
                    name=questionary.text(
                        "What's the attribute name?",
                        validate=lambda val: "That attribute need a name!"
                        if len(val) == 0 else True,
                        default=attribute["name"]
                    ),
                    description=questionary.text(
                        "What's the attribute description?",
                        validate=lambda val: "That attribute need a description!"
                        if len(val) == 0 else True,
                        default=attribute["description"]
                    ),
                    type=questionary.text(
                        "What's the attribute type?",
                        default=attribute["type"]
                    ),
                    identifier=questionary.confirm(
                        "That attribute should be consider as an identifier?",
                        default=attribute["identifier"]
                    )
                ).ask()

                attrs.append(attribute)

            print("\r\nThat's all for the existing attributes.")
        create_attr = questionary.confirm(
            "Would you like to add another attribute?", default=True).ask()

        while create_attr:
            attribute = questionary.form(
                name=questionary.text(
                    "What's the attribute name?",
                    validate=lambda val: "That attribute need a name!"
                    if len(val) == 0 else True,
                ),
                description=questionary.text(
                    "What's the attribute description?",
                    validate=lambda val: "That attribute need a description!"
                    if len(val) == 0 else True,
                ),
                type=questionary.text(
                    "What's the attribute type?",
                    default="str"
                ),
                identifier=questionary.confirm(
                    "That attribute should be consider as an identifier?",
                    default=False)
            ).ask()

            attrs.append(attribute)
            print("")
            create_attr = questionary.confirm(
                "Would you like to add another attribute?").ask()

        return attrs

    @staticmethod
    def create_usecase_form(usecase_update=None):
        usecase = {}
        print("")
        if usecase_update is None:
            usecase["type_"] = questionary.select(
                "What types of usecase this will be?",
                choices=["Create", "Read", "Update", "Delete", "List", "Custom"],
                use_pointer=True,
            ).ask()
        elif usecase_update is not None and "Custom" not in usecase_update.type_:
            print("Only the update for Custom usecase are allowed.")
            exit(1)

        input_attrs = None
        output_attrs = None

        type_ = usecase["type_"] if usecase_update is None else usecase_update.type_
        if usecase_update is not None:
            input_attrs = usecase_update.input_attrs
            output_attrs = usecase_update.output_attrs

        if "Custom" == type_:
            if usecase_update is None:
                usecase["name"] = questionary.text(
                    "What's the usecase name?",
                    validate=lambda val: "That usecase need a name!"
                    if len(val) == 0 else True,
                ).ask()

            usecase["description"] = questionary.text(
                "What's the usecase description?",
                validate=lambda val: "That usecase need a description!"
                if len(val) == 0 else True,
                default=usecase_update.description
                if usecase_update is not None else ""
            ).ask()

            print("\r\nLet's fill the inputs")
            usecase["input_attrs"] = Factory._create_attributes_form(input_attrs)
            print("\r\nLet's fill the outputs")
            usecase["output_attrs"] = Factory._create_attributes_form(output_attrs)

        return usecase
