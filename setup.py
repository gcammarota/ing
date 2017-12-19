#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017-2018 Giuseppe Cammarota.
#

from setuptools import setup, find_packages


version = "0.1.0"


setup(
    name="ing",
    version=version,
    author="Giuseppe Cammarota",
    author_email="g.cammarota@gmail.com",
    description="This is a proof of concept package for visualizing personal finances.",
    license="Apache 2.0",
    url='https://github.com/gcammarota/ing',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'dash',
        'dash_core_components',
        'dash_html_components',
        'plotly',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Finance',
    ],
    keywords='',
    entry_points={
        'console_scripts': [
            'ing = ing.app:run',
        ],
    },
)
