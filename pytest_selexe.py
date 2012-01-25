"""
py.test plugin to automatically find and execute selenese *.sel tests
"""
__version__ = '0.2'

import py, pytest, sys, logging
from selexe import SelexeRunner, SelexeError, cmdargs


def pytest_addoption(parser):
    group = parser.getgroup("general")
    for args, kw in cmdargs.options:
        group.addoption(*args, **kw)


def pytest_configure(config):
    ll = config.option.logging.upper()
    try:
        logLevel = getattr(logging, ll)
    except AttributeError:
        raise ValueError('invalid logging level "%s" specified! Valid values are "warning" (default), "info, "debug"' %
                         config.option.logging)
    logging.basicConfig(level=logLevel)


def pytest_report_header(config):
    if config.option.baseuri:
        return "\nOverriding base URI for all Selenium tests to %s\n" % config.option.baseuri


def pytest_collect_file(path, parent):
    if parent.config.option.selexe and path.ext == ".sel":
        return SeleneseFile(path, parent)


class SeleneseFile(pytest.Item, pytest.File):
#    def __init__(self, path, parent):
#        super(SeleneseFile, self).__init__(path, parent)
#        import pdb;pdb.set_trace()
#        #self.filename = path.strpath

    def runtest(self):
        selexe = SelexeRunner(self.fspath.strpath, baseuri=self.config.option.baseuri,
                              fixtures=self.config.option.fixtures)
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

