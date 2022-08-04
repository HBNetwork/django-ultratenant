#!/usr/bin/env python

"""The setup script."""


import pathlib

from setuptools import find_packages, setup

readme = pathlib.Path("README.md").read_text()
history = pathlib.Path("CHANGELOG.md").read_text()
requirements = ["dj-database-url>=1.0.0", "python-decouple>=3.6"]

test_requirements = ["pytest"]

setup(
    author="HBN3tw0rk",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Ultimate Django app for multi-tenant.",
    install_requires=requirements,
    license="GNU Lesser General Public License v2.1",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="ultratenant",
    name="django-ultratenant",
    packages=find_packages(include=["ultratenant", "ultratenant.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/HBN3tw0rk/django-ultratenant",
    version="0.0.1",
    zip_safe=False,
)
