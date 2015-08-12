#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


def version():
    from gocd_cli.commands import echo
    return echo.__version__


setup(
    name='gocd-cli.commands.echo',
    author='Björn Andersson',
    author_email='ba@sanitarium.se',
    license='MIT License',
    description='An example echo command',
    long_description=README,
    version=version(),
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'gocd-cli>=0.7,<1.0',
    ],
)
