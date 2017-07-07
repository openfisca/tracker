#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="Tracker",
    version="0.0.1",
    description="A Tracker of the OpenFisca Web API usage",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    author="",
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'OpenFisca-Web-API >= 6.0.0',
        ],
    extras_require = {
        'test': [
            'nose',
            ]
        },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
