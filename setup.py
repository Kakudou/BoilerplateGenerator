import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BoilerplateGenerator",
    version="0.0.0",
    description="Automatization of the boilerplate for my projects",
    url="https://gitlab.com/kakudou/BoilerplateGenerator",
    author="Kakudou",
    author_email="contact@kakudou.org",
    packages=setuptools.find_packages(),
    install_requires=["PyYaml",
                      "Jinja2",
                      "questionary",
                      "click",
    ],
    entry_points="""
        [console_scripts]
        BoilerplateGenerator=boilerplate_generator.__main__:boilerplate_generator
        """,
    classifiers=[
        "License::MIT License",
        "implemented-in::Python",
        "devel::Python",
        "devel::Clean Architecture",
        "devel::BDD"
        "devel::Tools",
        "devel::Gerkhin",
        "devel::Boilerplate",
    ],
    python_requires='>=3.8',
)
