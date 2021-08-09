# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Get the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()

# Get requirements
with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='json_schema_to_dash_forms',
    version='0.1.8',
    description='JSON schema to Dash forms',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Luiz Tauffer and Vinicius Camozzato Vaz',
    author_email='luiz@taufferconsulting.com',
    url='https://github.com/catalystneuro/json-schema-to-dash-forms',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.yml', '*.json']},
    install_requires=install_requires,
)
