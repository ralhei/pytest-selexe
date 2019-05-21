"""
Main pytest_selexe plugin module
"""
import pytest

from selexe import SelexeRunner, SelexeError, SelexeArgumentParser


def pytest_addoption(parser):
    """Extend pytest's arg parser by extensions specific to selexe"""
    group = parser.getgroup('selexe')
    SelexeArgumentParser.add_main_args(group.addoption)


def pytest_collect_file(path, parent):
    """Filter selenese files

    :param path: pathlib object, referring to a possible (selenese) file to be tested
    :param parent:
    :return: SeleneseFile instance in case path references a selenese file
    """
    if path.ext == ".sel":
        return SeleneseFile(path, parent)


class SeleneseFile(pytest.Item, pytest.File):
    def __init__(self, path, parent):
        super(SeleneseFile, self).__init__(path, parent)

    def collect(self):
        """No implementation needed here, there is only one test per selenium file."""

    def runtest(self):
        selexe = SelexeRunner(self.fspath.strpath, baseuri=self.config.option.baseuri,   # TODO: add more options
                              fixtures=self.config.option.selexe_fixtures)
        res = selexe.run()
        if res:
            raise SelexeError(res)

    def repr_failure(self, excinfo):
        """ called when self.runtest() raises an exception. """
        if isinstance(excinfo.value, SelexeError):
            return "\n".join([
                "selenium file %s failed" % self.fspath,
                "%r" % excinfo.value.args[0]
            ])
        return super(SeleneseFile, self).repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, 0, ''
