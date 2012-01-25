from setuptools import setup

from pytest_selexe import __version__

setup(
    name='pytest-selexe',
    description='pytest plugin for selexe, a tool to directly execute selenium files',
    long_description=open("README.txt").read(),
    url='http://pypi.python.org/pypi/pytest-selexe/',
    author='Ralph Heinkel',
    author_email='rh@ralph-heinkel.com',
    version=__version__,
    py_modules = ['pytest_selexe'],
    entry_points = {
        'pytest11': [
            'selexe = pytest_selexe',
            ]
        },
    install_requires = ['pytest>=2.0', 'selexe'],
    license='MIT license',
    platforms=['unix', 'linux', 'cygwin'],
    classifiers=[  'Development Status :: 2 - Pre-Alpha',
                   'Environment :: Console',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: POSIX',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: MacOS :: MacOS X',
                   'Programming Language :: Python',
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Testing',
                   ],
    )
