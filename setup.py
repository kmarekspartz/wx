#!/usr/bin/env python
"""
Setup file.
"""

from setuptools import setup, find_packages


setup(
    name='wx',
    version='0.1',
    description='',
    long_description=open('README.md').read(),
    author='Kyle Marek-Spartz',
    author_email='kyle.marek.spartz@gmail.com',
    py_modules=['wx'],
    url='',
    include_package_data=True,
    packages=find_packages(exclude=['tests*']),
    install_requires=['flask-peewee'],
    test_suite='nose.collector',
    classifiers=["Private :: Do Not Upload"],  # TODO
    license=''  # TODO
)
