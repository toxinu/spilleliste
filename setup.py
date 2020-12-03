#!/usr/bin/env python2
# coding: utf-8

import os
import sys
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version():
    VERSIONFILE = 'spilleliste/__init__.py'
    initfile_lines = open(VERSIONFILE, 'rt').readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='spilleliste',
    version=get_version(),
    description="Spilleliste, share your beautiful playlist.",
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='toxinu',
    author_email='toxinu@gmail.com',
    url='https://github.com/toxinu/spilleliste',
    keywords='music',
    packages=[
        'spilleliste',
        'spilleliste.externals',
        'spilleliste.connectors'],
    scripts=['scripts/spilleliste'],
    install_requires=[
        'requests',
        'docopt',
        'requests',
        'jinja2',
        'isit'
    ],
    include_package_data=True,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7')
)
