#!/usr/bin/env python

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-selexe',
    version='0.3.0a1',
    author='Ralph Heinkel',
    author_email='rh@ralph-heinkel.com',
    maintainer='Ralph Heinkel',
    maintainer_email='rh@ralph-heinkel.com',
    license='MIT',
    url='https://github.com/ralhei/pytest-selexe',
    description='py.test plugin for selexe, a tool to directly execute selenese files created by Selenium IDE',
    long_description=read('README.md'),
    py_modules=['pytest_selexe'],
    python_requires='>=3.6',
    install_requires=['pytest>=3.5.0', 'selexe>=0.3.0a1'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [    # pytest11 is the default entrypoint namespace for pytest!
            'selexe = pytest_selexe',
        ],
    },
)
