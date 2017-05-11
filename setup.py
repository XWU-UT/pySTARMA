"""
Project: 
File: setup

Created by Scrat on 11.05.2017
"""

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pySTARMA',
    version='0.1.0',
    description='todo',
    long_description=readme,
    author='Andreas Wolf',
    author_email='andreas.wolf.ke@gmail.com',
    url='https://github.com/scrat-online/pySTARMA.git',
    license=license,
    packages=find_packages()
)