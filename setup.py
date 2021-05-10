"""This file contains your package's metadata and dependencies."""

from setuptools import find_packages, setup

setup(
    name = "OpenFisca-Tracker",
    version = "0.4.2",
    author = "OpenFisca Team",
    author_email = "contact@openfisca.org",
    classifiers = [
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        ],
    description = "A Tracker of the OpenFisca Web API usage",
    license = "http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    include_package_data = True,
    install_requires = [
        "grequests == 0.6.0",
        ],
    extras_require={
        "dev": [
            "autopep8 >= 1.5.4, < 2.0.0",
            "flake8 >= 3.8.0, < 4.0.0",
            "flake8-bugbear >= 20.1.0, < 21.0.0",
            "flake8-builtins >= 1.5.0, < 2.0.0",
            "flake8-coding >= 1.3.0, < 2.0.0",
            "flake8-commas >= 2.0.0, < 3.0.0",
            "flake8-comprehensions >= 3.2.0, < 4.0.0",
            "flake8-docstrings >= 1.5.0, < 2.0.0",
            "flake8-import-order >= 0.18.0, < 1.0.0",
            "flake8-print >= 3.1.0, < 5.0.0",
            "flake8-quotes >= 3.2.0, < 4.0.0",
            "flake8-simplify >= 0.9.0, < 1.0.0",
            "flake8-use-fstring >= 1.1.0, < 2.0.0",
            "pylint >= 2.6.0, < 3.0.0",
            "pycodestyle >= 2.6.0, < 3.0.0",
            "pytest >= 5.0.0, < 6.0.0",
            ],
        },
    packages = find_packages(),
    )
