#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import filechooser

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = filechooser.__version__

if sys.argv[-1] == 'publish':
    os.system('cd docs && make html')
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='django-filechooser',
    version=version,
    description="""jQuery Filechooser for Django projects""",
    long_description=readme + '\n\n' + history,
    author='Martin van Wingerden',
    author_email='martinvw@gmail.com',
    url='https://github.com/martinvw/django-filechooser',
    download_url="https://github.com/martinvw/django-filechooser/archive/v0.1.0.tar.gz",
    packages=[
        'filechooser',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='django-filechooser',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
