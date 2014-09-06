#!/usr/bin/env python3
from setuptools import setup, find_packages

import licensechecker

setup(
    name='licensechecker',
    version=licensechecker.__version__,
    description='License checker for open source project',
    long_description='', # FIXME: Convert README.md to README.rst
    url='https://github.com/czchen/license-checker',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'license-checker = licensechecker.console:main',
        ]
    }
)
