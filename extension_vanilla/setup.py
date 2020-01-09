# Copyright 2020 Paul Hansen
# Unauthorized copying of this file is strictly prohibited
# Proprietary and confidential

import os
import sys
import pathlib
import subprocess
import warnings

import setuptools

install_requires = []

setuptools.setup(
    name = "extension_vanilla",
    version = "0.0.1", #get_version(),
    author = "Paul Hansen",
    description = ("Vanilla Python extension with ctypes"),
    packages = setuptools.find_packages("src", exclude=("tests")),
    package_dir = {'':"src"},
    ext_modules=[setuptools.Extension("nativepkg", ["src/nativepkg/interface.cpp"])], # this one works
    # headers=['src/nativepkg/interface.hpp'],  # does not work
    include_package_data=True,
    install_requires = install_requires,
    python_requires = ">=3"
)
