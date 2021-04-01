import click
import collections

from boilerplate_generator.src\
    import VERSION

from boilerplate_generator.src.app.cli.view.project.create_project\
    import CreateProject
from boilerplate_generator.src.app.cli.view.project.read_project\
    import ReadProject
from boilerplate_generator.src.app.cli.view.project.update_project\
    import UpdateProject
from boilerplate_generator.src.app.cli.view.project.delete_project\
    import DeleteProject
from boilerplate_generator.src.app.cli.view.project.list_projects\
    import ListProjects

from boilerplate_generator.src.app.cli.view.feature.create_feature\
    import CreateFeature
from boilerplate_generator.src.app.cli.view.feature.read_feature\
    import ReadFeature
from boilerplate_generator.src.app.cli.view.feature.update_feature\
    import UpdateFeature
from boilerplate_generator.src.app.cli.view.feature.delete_feature\
    import DeleteFeature
from boilerplate_generator.src.app.cli.view.feature.list_features\
    import ListFeatures

from boilerplate_generator.src.app.cli.view.constraint.create_constraint\
    import CreateConstraint
from boilerplate_generator.src.app.cli.view.constraint.read_constraint\
    import ReadConstraint
from boilerplate_generator.src.app.cli.view.constraint.update_constraint\
    import UpdateConstraint
from boilerplate_generator.src.app.cli.view.constraint.delete_constraint\
    import DeleteConstraint
from boilerplate_generator.src.app.cli.view.constraint.list_constraints\
    import ListConstraints

from boilerplate_generator.src.app.cli.view.entity.create_entity\
    import CreateEntity
from boilerplate_generator.src.app.cli.view.entity.read_entity\
    import ReadEntity
from boilerplate_generator.src.app.cli.view.entity.update_entity\
    import UpdateEntity
from boilerplate_generator.src.app.cli.view.entity.delete_entity\
    import DeleteEntity
from boilerplate_generator.src.app.cli.view.entity.list_entities\
    import ListEntities

from boilerplate_generator.src.app.cli.view.usecase.create_crudl\
    import CreateCrudl
from boilerplate_generator.src.app.cli.view.usecase.create_usecase\
    import CreateUsecase
from boilerplate_generator.src.app.cli.view.usecase.read_usecase\
    import ReadUsecase
from boilerplate_generator.src.app.cli.view.usecase.update_usecase\
    import UpdateUsecase
from boilerplate_generator.src.app.cli.view.usecase.delete_usecase\
    import DeleteUsecase
from boilerplate_generator.src.app.cli.view.usecase.list_usecases\
    import ListUsecases

from boilerplate_generator.src.app.cli.view.project.generate_structure\
    import GenerateStructure
from boilerplate_generator.src.app.cli.view.feature.generate_feature\
    import GenerateFeature
from boilerplate_generator.src.app.cli.view.constraint.generate_constraint\
    import GenerateConstraint
from boilerplate_generator.src.app.cli.view.entity.generate_entity\
    import GenerateEntity
from boilerplate_generator.src.app.cli.view.usecase.generate_usecase\
    import GenerateUsecase
from boilerplate_generator.src.app.cli.view.usecase.generate_crudl\
    import GenerateCrudl
from boilerplate_generator.src.app.cli.view.project.generate_project\
    import GenerateProject
