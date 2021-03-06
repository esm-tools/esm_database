#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["sqlalchemy" ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Dirk Barbi",
    author_email='dirk.barbi@awi.de',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="All the stuff for database access needed for ESMTools",
    entry_points={
        'console_scripts': [
            'esm_database=esm_database.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v2",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='esm_database',
    name='esm_database',
    packages=find_packages(include=['esm_database', 'esm_database.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dbarbi/esm_database',
    version='5.0.0',
    zip_safe=False,
)
