py.test plugin for directly executing selenium files using the `selexe module <http://pypi.python.org/pypi/selexe>`_.

Usage
---------

install via::

    easy_install pytest-selexe # or
    pip install pytest-selexe

and then type::

    py.test --selexe

to activate selenium code execution. Every file ending in ``.sel`` will be
discovered and checked, starting from the command line arguments. Or just select the desired ones::

    py.test --selexe yourseleniumfile.sel

More documentation will come soon.

