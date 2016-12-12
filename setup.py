#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='figurePXJ',
    version='0.0.0',
    author='Xingjie Pan',
    author_email='xingjiepan@gmail.com',
    url='https://github.com/xingjiepan/figurePXJ',
    packages=[
        'figurePXJ',
    ],
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    description='A toolkit for making figures with styles that PXJ likes.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
    ],
)
