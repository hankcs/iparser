# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-11 20:54
from os.path import abspath, join, dirname

from setuptools import find_packages, setup


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='iparser',
    version='0.1.8',
    description='Integrated and Industrial Strength Dependency Parser',
    long_description=long_description,
    url='https://github.com/hankcs/iparser',
    author='hankcs',
    author_email='hankcshe@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    keywords='dependency parser',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=['dynet', 'iparsermodels>=0.1.0'],
    dependency_links=[
        'http://storage.live.com/items/D4A741A579C555F7!65701:/iparsermodels-0.1.0.tar.gz#egg=iparsermodels-0.1.0'],
    entry_points={
        'console_scripts': [
            'iparser=iparser.main:main',
        ],
    },
)
