#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ft991cat-Dateranoth",
    version="0.0.1",
    author="Dateranoth",
    author_email="dateranoth@hotmail.com",
    description="A package to connect to Yaesu FT-991/A",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dateranoth/ft991cat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)