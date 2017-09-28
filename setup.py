#!/usr/bin/env python
from setuptools import setup

setup(
    name="drf-mongo-filters",
    packages=["drf_mongo_filters",],
    version="1.1",
    install_requires=["Django >= 1.11",
                      "mongoengine >= 0.13",
                      "djangorestframework >= 3.5.3"],
    # metadata for upload to PyPI
    author="Maxim Vasiliev",
    author_email="qwiglydee@gmail.com",
    description="Filtering support for Django Rest Framework Mongoengine.",
    keywords=["mongoengine", "django rest framework", "filtering"],
    url="https://github.com/qwiglydee/drf-mongo-filters",
    download_url="https://github.com/qwiglydee/drf-mongo-filters/releases",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
