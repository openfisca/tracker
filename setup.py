#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="OpenFisca-Tracker",
    version="0.4.0",
    description="A Tracker of the OpenFisca Web API usage",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    author="",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'grequests == 0.6.0'
        ],
    extras_require={
        'test': [
            'pytest',
            'flake8',
            ]
        },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        ]
    )
