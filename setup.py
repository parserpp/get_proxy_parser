#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import ast
from setuptools import setup, find_packages

with open('README.md', "r", encoding='utf-8') as readme_file:
    readme = readme_file.read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('__init__.py', 'rb') as f:
    version = str(
        ast.literal_eval(
            _version_re.search(f.read().decode('utf-8')).group(1)))

with open('requirements_dev.txt', 'r', encoding='utf-8') as fin:
    requirements = [i.strip() for i in fin.readlines()]


setup(
    name='gproxy',
    version=version,
    description="get proxy",
    long_description=readme,
    author="sanbo",
    author_email='sanbo.xyz@gmail.com',
    url='https://github.com/parserpp/get_proxy_parser',
    packages=find_packages(),
    package_dir={},
    entry_points={'console_scripts': ['gproxy=cli:main']},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=True,
    keywords='gproxy',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.10.2',
    ],
)
