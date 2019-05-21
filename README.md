# pytest-selexe

py.test plugin for selexe, a tool to directly execute selenese files created by Selenium IDE


# Features

* TODO


# Requirements

* TODO


# Installation

"pytest-selexe" can be installed via `pip` from `PyPI`:

    $ pip install pytest-selexe

## Geckodriver 

Additionally 'geckodriver' needs to be installed. 
The simplest method is to download it from https://github.com/mozilla/geckodriver/releases
and unpack the binary tar.gz file into a directory contained in PATH (the `geckodriver`-executable
should be the only file contained in the package).

# Usage

    $ pytest --baseuri http://localhost:8080 *.sel

where `http://localhost:8080` is the server running the application you'd like to test.

# TODO

# Contributing

Contributions are very welcome. Tests can be run with `tox`, please ensure
the coverage at least stays the same before you submit a pull request.

# License

Distributed under the terms of the `MIT` license, "pytest-selexe" is free and open source software
