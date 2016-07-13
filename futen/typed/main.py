from os import path
from collections import namedtuple
from futen import get_netlocs, execute
from benchmark_tools.timer import Timer

#bg: all test files should be in current directory when tests run


def test_get_netlocs()->Void:
    testfile = path.join(path.dirname(__file__), 'ssh.config')
    expect = {'web': '2200', 'app': '2201', 'db': '2202'}
    with open(testfile) as fd:
        actual = get_netlocs(fd.readlines())
        if expect == actual:
            return
        else:
            raise AssertionError("'%s' is not equal to '%s'" % (expect, actual))

def test_template_render()->Void:
    testfile = path.join(path.dirname(__file__), 'ssh.config')
    template = path.join(path.dirname(__file__), 'inventory_template')
    expectfile = path.join(path.dirname(__file__), 'inventory_expect')
    with open(expectfile) as fd:
        expect = ''.join(fd.readlines())
    with open(testfile) as fd:
        lines = fd.readlines()
        args_mock = namedtuple(
            'ArgumentParserMock',
            ['template_file']
        )(template)
        result = execute(lines, args_mock)
        if result == expect:
            return
        else:
            raise AssertionError("'%s' is not equal to '%s'" % (expect, actual))

t = Timer()
with t:
  main()
