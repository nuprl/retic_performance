from os import path
from collections import namedtuple
from futen import get_netlocs, execute
from benchmark_tools.Timer import Timer

#bg: all test files should be in current directory when tests run


def main()->Void:
    testfile = path.join(path.dirname(__file__), 'ssh.config.dat')
    expect = {'web': '2200', 'app': '2201', 'db': '2202'}
    with open(testfile) as fd:
        actual = get_netlocs(fd.readlines())
        if expect != actual:
            raise AssertionError("'%s' is not equal to '%s'" % (expect, actual))

    testfile = path.join(path.dirname(__file__), 'ssh.config.dat')
    template = path.join(path.dirname(__file__), 'inventory_template.dat')
    expectfile = path.join(path.dirname(__file__), 'inventory_expect.dat')
    with open(expectfile) as fd:
        expect = ''.join(fd.readlines())
    with open(testfile) as fd:
        lines = fd.readlines()
        args_mock = namedtuple(
            'ArgumentParserMock',
            ['template_file']
        )(template)
        result = execute(lines, args_mock)
        if result != expect:
            raise AssertionError("'%s' is not equal to '%s'" % (expect, actual))
    return


t = Timer()
with t:
    main()
