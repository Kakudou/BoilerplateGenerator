# BoilerplateGenerator

---------------------------------------------------

<center><a href="https://gitmoji.carloscuesta.me">
  <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" alt="Gitmoji">
</a></center>

---------------------------------------------------

## TL;DR

[[_TOC_]]

# BoilerplateGenerator

BoilerplateGenerator is a robust and flexible framework designed to streamline the generation of boilerplate code for projects adhering to advanced architectural and development principles. By integrating Clean Architecture, BDD, TDD, the Port-Adapter pattern, and more, BoilerplateGenerator accelerates development, promotes best practices, and ensures high-quality, maintainable software. 

## Why BoilerplateGenerator?
Manually implementing complex architectural patterns can be time-consuming and error-prone. BoilerplateGenerator addresses this challenge by automating the creation of foundational project structures while adhering to:

- **Behavior-Driven Development (BDD)**
- **Gherkin Feature and Constraint Files**
- **Test-Driven Development (TDD)**
- **Clean Architecture Principles**
- **Port-Adapter (Hexagonal) Pattern**
- **Builder Pattern**

The framework not only saves time but also enforces consistency, scalability, and maintainability across projects, making it invaluable for modern software engineering.

## Core Architectural Concepts
BoilerplateGenerator is built around a carefully selected set of architectural principles, each chosen for its contribution to creating flexible, robust, and future-proof applications. Here’s an in-depth look at the concepts and their synergy:

### 1. **Behavior-Driven Development (BDD)**
BDD promotes collaboration between developers, testers, and business stakeholders by focusing on application behavior described in plain language. BoilerplateGenerator incorporates this approach by generating Gherkin-based feature files and constraints.

#### Advantages:
- **Shared Understanding:** Feature files serve as a single source of truth, bridging the gap between technical and non-technical stakeholders.
- **Executable Documentation:** These files double as automated tests, ensuring that requirements are always up to date.
- **Improved Quality:** By starting with behavior definitions, development aligns more closely with business goals.

#### Implementation Details:
BoilerplateGenerator scaffolds Gherkin files that integrate seamlessly with testing frameworks, enabling quick creation of executable specifications that drive development. The Gherkin constraints enforce functional boundaries, ensuring clarity and preventing regression.

### 2. **Clean Architecture**
Clean Architecture emphasizes the separation of concerns, dividing an application into distinct layers such as entities, use cases, and interfaces. BoilerplateGenerator enforces this structure, ensuring:

#### Advantages:
- **Independence from Frameworks:** Core logic remains unaffected by changes in external technologies.
- **Testability:** Each layer can be tested in isolation, simplifying debugging and validation.
- **Scalability:** The modular design allows for incremental growth without introducing technical debt.

#### Implementation Details:
The generated structure includes:
- **Entities:** Representing core business logic, free of external dependencies.
- **Use Cases:** Orchestrating interactions between entities and external systems.
- **Adapters:** Bridging the gap between core logic and infrastructure (e.g., APIs, databases).

By default, BoilerplateGenerator ensures high cohesion within layers and low coupling between them, making it easier to adapt to future changes.

### 3. **Port-Adapter (Hexagonal) Pattern**
The Port-Adapter pattern extends Clean Architecture by emphasizing dependency inversion. This ensures that the core application logic remains independent of external systems.

#### Advantages:
- **Decoupling:** Clear interfaces allow for seamless replacement or modification of external dependencies.
- **Flexibility:** Adapters can be tailored to various contexts (e.g., switching databases or APIs).
- **Resilience:** The core remains stable, even as the external environment evolves.

#### Implementation Details:
BoilerplateGenerator scaffolds:
- **Ports:** Interfaces defining how external systems interact with the core.
- **Adapters:** Concrete implementations of these interfaces, isolating infrastructure-specific logic.

This approach allows developers to swap out implementations (e.g., transitioning from REST to GraphQL) with minimal impact on the core application.

### 4. **Builder Pattern**
The Builder pattern simplifies the construction of complex objects by breaking the instantiation process into manageable steps. BoilerplateGenerator leverages this pattern for creating DTOs, configuration objects, and other entities.

#### Advantages:
- **Immutability:** Encourages the creation of immutable objects, reducing bugs.
- **Readability:** Improves code clarity by making object creation self-explanatory.
- **Flexibility:** Supports varying configurations without polluting constructors.

#### Implementation Details:
For entities and DTOs, BoilerplateGenerator produces builders that:
- Allow step-by-step construction of objects.
- Support validation during the build process, ensuring consistency.
- Provide clear APIs for configuring optional parameters.

This approach is particularly valuable in complex domains where objects have numerous optional attributes or dependencies.

### 5. **Gherkin Feature and Constraints**
BoilerplateGenerator integrates Gherkin to define application behavior in natural language, ensuring alignment between requirements and implementation.

#### Advantages:
- **Human-Readable Tests:** Scenarios are easy for all stakeholders to understand.
- **Automation-Friendly:** Gherkin files integrate directly with testing frameworks.
- **Traceability:** Feature files act as living documentation, reducing reliance on outdated specs.

#### Implementation Details:
The framework generates:
- **Feature Files:** Containing user stories and scenarios written in Gherkin syntax.
- **Constraint Files:** Defining specific rules or boundaries that govern system behavior.

These artifacts ensure that development stays aligned with business objectives while enabling robust automated testing.

### 6. **Test-Driven Development (TDD)**
TDD is a cornerstone of the framework, driving the creation of reliable and maintainable software.

#### Advantages:
- **Fewer Bugs:** Writing tests first ensures code correctness from the outset.
- **Refactoring Confidence:** Tests act as a safety net, allowing for fearless refactoring.
- **Cleaner Code:** Focused test cases lead to simpler, more modular implementations.

#### Implementation Details:
BoilerplateGenerator scaffolds test cases alongside the generated code, encouraging:
- The creation of unit tests for core logic.
- Integration tests for verifying interactions between components.
- End-to-end tests based on Gherkin scenarios.

By embedding TDD practices, the framework ensures that your codebase remains robust and maintainable over time.

## Architectural Synergy
The true strength of BoilerplateGenerator lies in how these principles work together to create a unified, efficient development process:

- **BDD and Gherkin:** Ensure that requirements are clear, testable, and executable.
- **Clean Architecture:** Provides a solid foundation for organizing code.
- **Port-Adapter Pattern:** Decouples core logic from external dependencies, enhancing flexibility.
- **Builder Pattern:** Simplifies the creation of complex objects, reducing boilerplate.
- **TDD:** Promotes high-quality, testable implementations from the start.

Each principle amplifies the benefits of the others. For example, Gherkin feature files drive TDD by serving as executable specifications, while the Port-Adapter pattern ensures that tests remain focused on business logic rather than infrastructure concerns. This creates a self-reinforcing cycle of clarity, quality, and maintainability.

## Getting Started

### Installation

To install BoilerplateGenerator, it's easy as consuming the pyproject.toml file.

Run the following command or any other method you prefer to install the package.

```bash
git clone https://github.com/kakudou/BoilerplateGenerator.git
cd BoilerplateGenerator
python -m venv .venv --prompt BoilerplateGenerator
source .venv/bin/activate
pip install .
``` 

### Usage

To generate a new project, run the following command:

You can access the help menu by running the following command:

```bash
boilerplate-generator --help
```

and show an example usage using:

```bash
BoilerplateGenerator usage
```

The whole list of commands is:

```bash
Usage: BoilerplateGenerator [OPTIONS] COMMAND [ARGS]...

  CLI tool to manage the boilerplate of projects, version v0.0.0

Options:
  -h, --help  Show this message and exit.

Commands:
  ----------------------projects----------------------
  create-project                  Create a Project.
  read-project                    Read a Project.
  update-project                  Update a Project.
  delete-project                  Delete a Project.
  list-projects                   List all Projects
  ----------------------features----------------------
  create-feature                  Create a Feature.
  read-feature                    Read a Feature.
  update-feature                  Update a Feature.
  delete-feature                  Delete a Feature.
  list-features                   List all Features.
  ----------------------constraints----------------------
  create-constraint               Create a Constraint.
  read-constraint                 Read a Constraint.
  update-constraint               Update a Constraint.
  delete-constraint               Delete a Constraint.
  list-constraints                List all Constraints.
  ----------------------entities----------------------
  create-entity                   Create a Entity.
  read-entity                     Read a Entity.
  update-entity                   Update a Entity.
  delete-entity                   Delete a Entity.
  list-entities                   List all Entities.
  ----------------------usecases----------------------
  create-crudl                    Create CRUDL for an Entity.
  create-usecase                  Create a Usecase.
  read-usecase                    Read a Usecase.
  update-usecase                  Update a Usecase.
  delete-usecase                  Delete a Usecase.
  list-usecases                   List all Usecases.
  ----------------------generate----------------------
  generate-structure              Generate the structure of a Project.
  generate-feature                Generate a feature.
  generate-constraint             Generate a constraint.
  generate-entity                 Generate an entity.
  generate-crudl                  Generate the crudl.
  generate-usecase                Generate a usecase.
  generate-project                Generate everything, the whole Project.
  ----------------------usage----------------------
  usage                           Common Usage.
```

The main logic of the framework is to create your project, features, constraints, entities, usecases using the `create` commands, they will be written in a yaml file.
And then you can generate all or part of them using the `generate` commands.

You will be guided through each command by a CLI interface and formularies. 
You can also do all the CRUDL operations for each of your components.

Most of the time, the only code you will have to write:
  - pytest for each features and constraints
  - Custom usecases (meaning other than simple CRUDL operations)
  - Validators for your inputs contracts

And almost nothing else, at least for the core engine, interfaces, and adapters.
This mean you will need to implement code for the app layer(IHM, CLI, API, etc.) and the infrastructure layer (DB, API, etc.)
By default only InMemory repositories are implemented, you will have to implement the others.
And the adapters using the ports from the core engine.

If you want to see an example of a generated project, you can check the source code of BoilerplateGenerator itself.
It's not the exact representation of the output since it was generated using the PoC version of the framework, but it's close enough.

Remember, that tool is a work in progress and a personal framework, so it's not perfect and will not fit all your needs, it's made initially for my own use, but I'm sharing it with you in case it can help you.
Most of the time, my python projects are using this framework, so it's a good way to see how it works, and an easy way to contribute with them.

## Conclusion
BoilerplateGenerator is more than just a tool—it’s a philosophy-driven framework that embodies the best practices of modern software engineering. By automating the creation of well-structured codebases, it empowers developers to focus on solving real problems rather than wrestling with repetitive tasks.

Adopting BoilerplateGenerator means embracing a development approach that prioritizes scalability, maintainability, and collaboration. Whether you’re building a small application or a large enterprise system, BoilerplateGenerator provides the foundation you need to succeed.


