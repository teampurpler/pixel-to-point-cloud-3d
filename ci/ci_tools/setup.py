from setuptools import find_packages, setup

setup(
    name="ci_tools",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "black",
        "flake8",
        "GitPython",
        "isort",
        "jupyter-book",
        "jupytext",
        "mypy",
        "pylint",
        "pyright",
    ],
)
