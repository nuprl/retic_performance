#!/N/u/zmahmoud/Karst/Python-3.4.3/python

# Sets up a list of benchmarks (or all benchmarks) for `brun`
#
# Usage:
#    ./setup_karst.py
# or:
#    ./setup_karst.py <dir> ...
# where each `<dir>` is a benchmark directory (tho, we'll double check for you)
#
# This script:
# - makes all the configurations
# - sets up directories that `brun` expects
# - makes a worklist of configurations to run

## -----------------------------------------------------------------------------
## imports

import ast
import copy
import glob
import itertools
import os
import shutil
import subprocess
import sys

## -----------------------------------------------------------------------------
## constants

USER      = "zmahmoud"
BASEPATH  = "/N/u/%s/Karst" % USER
PYTHON    = "%s/Python-3.4.3/python" % BASEPATH
RETIC     = "%s/reticulated/retic.py" % BASEPATH
RP        = "%s/retic_performance" % BASEPATH
TOOLS     = "%s/benchmark_tools/benchmark_tools" % BASEPATH
READER    = "%s/Reader.py" % TOOLS
TIMER     = "%s/Timer.py"  % TOOLS

BENCHMARK = "Benchmark"
BOTH      = "both"
MAIN      = "main.py"
TEST      = "Test"
TYPED     = "typed"

KARST_OUTPUT = "karst_output.txt"
KARST_INPUT  = "karst_input.txt"

LINES_PER_KARST_FILE = 100000
# Keep it small enough to 'quickly' read/write files of this length

## -----------------------------------------------------------------------------
## from astor
def enclose(enclosure):
    def decorator(func):
        def newfunc(self, node):
            self.write(enclosure[0])
            func(self, node)
            self.write(enclosure[-1])
        return newfunc
    return decorator

def _getsymbol(mapping, map_dict=None, type=type):
    """This function returns a closure that will map a
    class type to its corresponding symbol, by looking
    up the class name of an object.

    """
    if isinstance(mapping, str):
        mapping = mapping.split()
        mapping = list(zip(mapping[0::2],
                           (x.replace('_', ' ') for x in mapping[1::2])))
        mapping = dict(((getattr(ast, x), y) for x, y in mapping))
    if map_dict is not None:
        map_dict.update(mapping)

    def getsymbol(obj, fmt='%s'):
        return fmt % mapping[type(obj)]
    return getsymbol

all_symbols = {}

get_boolop = _getsymbol("""
    And and   Or or
""", all_symbols)

binops = """
    Add +   Mult *   LShift <<   BitAnd &
    Sub -   Div  /   RShift >>   BitOr  |
            Mod  %               BitXor ^
            FloorDiv //
            Pow **
"""
if sys.version_info >= (3, 5):
    binops += "MatMult @"


get_binop = _getsymbol(binops, all_symbols)

get_cmpop = _getsymbol("""
  Eq    ==   Gt >   GtE >=   In    in       Is    is
  NotEq !=   Lt <   LtE <=   NotIn not_in   IsNot is_not
""", all_symbols)

get_unaryop = _getsymbol("""
    UAdd +   USub -   Invert ~   Not not
""", all_symbols)

get_anyop = _getsymbol(all_symbols)

class ExplicitNodeVisitor(ast.NodeVisitor):

  def abort_visit(node):  # XXX: self?
    msg = 'No defined handler for node of type %s'
    raise AttributeError(msg % node.__class__.__name__)

  def visit(self, node, abort=abort_visit):
    """Visit a node."""
    method = 'visit_' + node.__class__.__name__
    visitor = getattr(self, method, abort)
    return visitor(node)

def to_source(node, indent_with=' ' * 4, add_line_information=False):
    generator = SourceGenerator(indent_with, add_line_information)
    generator.visit(node)
    return ''.join(str(s) for s in generator.result)

class SourceGenerator(ExplicitNodeVisitor):

    def __init__(self, indent_with, add_line_information=False):
        self.result = []
        self.indent_with = indent_with
        self.add_line_information = add_line_information
        self.indentation = 0
        self.new_lines = 0

    def write(self, *params):
        for item in params:
            if isinstance(item, ast.AST):
                self.visit(item)
            elif hasattr(item, '__call__'):
                item()
            elif item == '\n':
                self.newline()
            else:
                if self.new_lines:
                    if self.result:
                        self.result.append('\n' * self.new_lines)
                    self.result.append(self.indent_with * self.indentation)
                    self.new_lines = 0
                self.result.append(item)

    def conditional_write(self, *stuff):
        if stuff[-1] is not None:
            self.write(*stuff)

    def newline(self, node=None, extra=0):
        self.new_lines = max(self.new_lines, 1 + extra)
        if node is not None and self.add_line_information:
            self.write('# line: %s' % node.lineno)
            self.new_lines = 1

    def body(self, statements):
        self.indentation += 1
        for stmt in statements:
            self.visit(stmt)
        self.indentation -= 1

    def else_body(self, elsewhat):
        if elsewhat:
            self.write('\n', 'else:')
            self.body(elsewhat)

    def body_or_else(self, node):
        self.body(node.body)
        self.else_body(node.orelse)

    def signature(self, node):
        want_comma = []

        def write_comma():
            if want_comma:
                self.write(', ')
            else:
                want_comma.append(True)

        def loop_args(args, defaults):
            padding = [None] * (len(args) - len(defaults))
            for arg, default in zip(args, padding + defaults):
                self.write(write_comma, arg)
                self.conditional_write('=', default)

        loop_args(node.args, node.defaults)
        self.conditional_write(write_comma, '*', node.vararg)
        self.conditional_write(write_comma, '**', node.kwarg)

        kwonlyargs = getattr(node, 'kwonlyargs', None)
        if kwonlyargs:
            if node.vararg is None:
                self.write(write_comma, '*')
            loop_args(kwonlyargs, node.kw_defaults)

    def statement(self, node, *params, **kw):
        self.newline(node)
        self.write(*params)

    def decorators(self, node, extra):
        self.newline(extra=extra)
        for decorator in node.decorator_list:
            self.statement(decorator, '@', decorator)

    def comma_list(self, items, trailing=False):
        for idx, item in enumerate(items):
            if idx:
                self.write(', ')
            self.visit(item)
        if trailing:
            self.write(',')

    # Statements

    def visit_Assign(self, node):
        self.newline(node)
        for target in node.targets:
            self.write(target, ' = ')
        self.visit(node.value)

    def visit_AugAssign(self, node):
        self.statement(node, node.target, get_binop(node.op, ' %s= '),
                       node.value)

    def visit_ImportFrom(self, node):
        if node.module:
            self.statement(node, 'from ', node.level * '.',
                           node.module, ' import ')
        else:
            self.statement(node, 'from ', node.level * '. import ')
        self.comma_list(node.names)

    def visit_Import(self, node):
        self.statement(node, 'import ')
        self.comma_list(node.names)

    def visit_Expr(self, node):
        self.statement(node)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.decorators(node, 1)
        self.statement(node, 'def %s(' % node.name)
        self.signature(node.args)
        self.write(')')
        if getattr(node, 'returns', None) is not None:
            self.write(' ->', node.returns)
        self.write(':')
        self.body(node.body)

    def visit_ClassDef(self, node):
        have_args = []

        def paren_or_comma():
            if have_args:
                self.write(', ')
            else:
                have_args.append(True)
                self.write('(')

        self.decorators(node, 2)
        self.statement(node, 'class %s' % node.name)
        for base in node.bases:
            self.write(paren_or_comma, base)
        # XXX: the if here is used to keep this module compatible
        #      with python 2.6.
        if hasattr(node, 'keywords'):
            for keyword in node.keywords:
                self.write(paren_or_comma, keyword.arg, '=', keyword.value)
            self.conditional_write(paren_or_comma, '*', node.starargs)
            self.conditional_write(paren_or_comma, '**', node.kwargs)
        self.write(have_args and '):' or ':')
        self.body(node.body)

    def visit_If(self, node):
        self.statement(node, 'if ', node.test, ':')
        self.body(node.body)
        while True:
            else_ = node.orelse
            if len(else_) == 1 and isinstance(else_[0], ast.If):
                node = else_[0]
                self.write('\n', 'elif ', node.test, ':')
                self.body(node.body)
            else:
                self.else_body(else_)
                break

    def visit_For(self, node):
        self.statement(node, 'for ', node.target, ' in ', node.iter, ':')
        self.body_or_else(node)

    def visit_While(self, node):
        self.statement(node, 'while ', node.test, ':')
        self.body_or_else(node)

    def visit_With(self, node):
        if hasattr(node, "context_expr"):  # Python < 3.3
            self.statement(node, 'with ', node.context_expr)
            self.conditional_write(' as ', node.optional_vars)
            self.write(':')
        else:                              # Python >= 3.3
            self.statement(node, 'with ')
            count = 0
            for item in node.items:
                if count > 0:
                    self.write(" , ")
                self.visit(item)
                count += 1
            self.write(':')
        self.body(node.body)

    # new for Python 3.3
    def visit_withitem(self, node):
        self.write(node.context_expr)
        self.conditional_write(' as ', node.optional_vars)

    def visit_NameConstant(self, node):
        self.write(node.value)

    def visit_Pass(self, node):
        self.statement(node, 'pass')

    def visit_Print(self, node):
        # XXX: python 2.6 only
        self.statement(node, 'print ')
        values = node.values
        if node.dest is not None:
            self.write(' >> ')
            values = [node.dest] + node.values
        self.comma_list(values, not node.nl)

    def visit_Delete(self, node):
        self.statement(node, 'del ')
        self.comma_list(node.targets)

    def visit_TryExcept(self, node):
        self.statement(node, 'try:')
        self.body(node.body)
        for handler in node.handlers:
            self.visit(handler)
        self.else_body(node.orelse)

    # new for Python 3.3
    def visit_Try(self, node):
        self.statement(node, 'try:')
        self.body(node.body)
        for handler in node.handlers:
            self.visit(handler)
        if node.finalbody:
            self.statement(node, 'finally:')
            self.body(node.finalbody)
        self.else_body(node.orelse)

    def visit_ExceptHandler(self, node):
        self.statement(node, 'except')
        if node.type is not None:
            self.write(' ', node.type)
            self.conditional_write(' as ', node.name)
        self.write(':')
        self.body(node.body)

    def visit_TryFinally(self, node):
        self.statement(node, 'try:')
        self.body(node.body)
        self.statement(node, 'finally:')
        self.body(node.finalbody)

    def visit_Exec(self, node):
        dicts = node.globals, node.locals
        dicts = dicts[::-1] if dicts[0] is None else dicts
        self.statement(node, 'exec ', node.body)
        self.conditional_write(' in ', dicts[0])
        self.conditional_write(', ', dicts[1])

    def visit_Assert(self, node):
        self.statement(node, 'assert ', node.test)
        self.conditional_write(', ', node.msg)

    def visit_Global(self, node):
        self.statement(node, 'global ', ', '.join(node.names))

    def visit_Nonlocal(self, node):
        self.statement(node, 'nonlocal ', ', '.join(node.names))

    def visit_Return(self, node):
        self.statement(node, 'return')
        self.conditional_write(' ', node.value)

    def visit_Break(self, node):
        self.statement(node, 'break')

    def visit_Continue(self, node):
        self.statement(node, 'continue')

    def visit_Raise(self, node):
        # XXX: Python 2.6 / 3.0 compatibility
        self.statement(node, 'raise')
        if hasattr(node, 'exc') and node.exc is not None:
            self.write(' ', node.exc)
            self.conditional_write(' from ', node.cause)
        elif hasattr(node, 'type') and node.type is not None:
            self.write(' ', node.type)
            self.conditional_write(', ', node.inst)
            self.conditional_write(', ', node.tback)

    # Expressions

    def visit_Attribute(self, node):
        self.write(node.value, '.', node.attr)

    def visit_Call(self, node):
        want_comma = []

        def write_comma():
            if want_comma:
                self.write(', ')
            else:
                want_comma.append(True)

        self.visit(node.func)
        self.write('(')
        for arg in node.args:
            self.write(write_comma, arg)
        for keyword in node.keywords:
            self.write(write_comma, keyword.arg, '=', keyword.value)
        self.conditional_write(write_comma, '*', node.starargs)
        self.conditional_write(write_comma, '**', node.kwargs)
        self.write(')')

    def visit_Name(self, node):
        self.write(node.id)

    def visit_Str(self, node):
        self.write(repr(node.s))

    def visit_Bytes(self, node):
        self.write(repr(node.s))

    def visit_Num(self, node):
        # Hack because ** binds more closely than '-'
        s = repr(node.n)
        if s.startswith('-'):
            s = '(%s)' % s
        self.write(s)

    @enclose('()')
    def visit_Tuple(self, node):
        self.comma_list(node.elts, len(node.elts) == 1)

    @enclose('[]')
    def visit_List(self, node):
        self.comma_list(node.elts)

    @enclose('{}')
    def visit_Set(self, node):
        self.comma_list(node.elts)

    @enclose('{}')
    def visit_Dict(self, node):
        for key, value in zip(node.keys, node.values):
            self.write(key, ': ', value, ', ')

    @enclose('()')
    def visit_BinOp(self, node):
        self.write(node.left, get_binop(node.op, ' %s '), node.right)

    @enclose('()')
    def visit_BoolOp(self, node):
        op = get_boolop(node.op, ' %s ')
        for idx, value in enumerate(node.values):
            self.write(idx and op or '', value)

    @enclose('()')
    def visit_Compare(self, node):
        self.visit(node.left)
        for op, right in zip(node.ops, node.comparators):
            self.write(get_cmpop(op, ' %s '), right)

    @enclose('()')
    def visit_UnaryOp(self, node):
        self.write(get_unaryop(node.op), ' ', node.operand)

    def visit_Subscript(self, node):
        self.write(node.value, '[', node.slice, ']')

    def visit_Slice(self, node):
        self.conditional_write(node.lower)
        self.write(':')
        self.conditional_write(node.upper)
        if node.step is not None:
            self.write(':')
            if not (isinstance(node.step, ast.Name) and
                    node.step.id == 'None'):
                self.visit(node.step)

    def visit_Index(self, node):
        self.visit(node.value)

    def visit_ExtSlice(self, node):
        self.comma_list(node.dims, len(node.dims) == 1)

    def visit_Yield(self, node):
        self.write('yield')
        self.conditional_write(' ', node.value)

    # new for Python 3.3
    def visit_YieldFrom(self, node):
        self.write('yield from ')
        self.visit(node.value)

    @enclose('()')
    def visit_Lambda(self, node):
        self.write('lambda ')
        self.signature(node.args)
        self.write(': ', node.body)

    def visit_Ellipsis(self, node):
        self.write('...')

    def generator_visit(left, right):
        def visit(self, node):
            self.write(left, node.elt)
            for comprehension in node.generators:
                self.visit(comprehension)
            self.write(right)
        return visit

    visit_ListComp = generator_visit('[', ']')
    visit_GeneratorExp = generator_visit('(', ')')
    visit_SetComp = generator_visit('{', '}')
    del generator_visit

    @enclose('{}')
    def visit_DictComp(self, node):
        self.write(node.key, ': ', node.value)
        for comprehension in node.generators:
            self.visit(comprehension)

    @enclose('()')
    def visit_IfExp(self, node):
        self.write(node.body, ' if ', node.test, ' else ', node.orelse)

    def visit_Starred(self, node):
        self.write('*', node.value)

    @enclose('``')
    def visit_Repr(self, node):
        # XXX: python 2.6 only
        self.visit(node.value)

    def visit_Module(self, node):
        for stmt in node.body:
            self.visit(stmt)

    # Helper Nodes

    def visit_arg(self, node):
        self.write(node.arg)
        self.conditional_write(': ', node.annotation)

    def visit_alias(self, node):
        self.write(node.name)
        self.conditional_write(' as ', node.asname)

    def visit_comprehension(self, node):
        self.write(' for ', node.target, ' in ', node.iter)
        if node.ifs:
            for if_ in node.ifs:
                self.write(' if ', if_)

    def visit_arguments(self, node):
        self.signature(node)

## -----------------------------------------------------------------------------
## from benchmark_tools.Reader

def parse_ast(filename):
  with open(filename, "r") as f:
    return ast.parse(f.read(), filename=filename, mode='exec')

def all_configurations_args(typed_args):
  """
    bg: simplified, to just return fully-typed and fully-untyped
  """
  res = []
  l = len(typed_args.args)
  for b in [False, True]:
    new_args = copy.deepcopy(typed_args)
    if b:
      for j in range(l):
        new_args.args[j].annotation = None
    res.append(new_args)
  return res

def all_configurations_def(d):
  args = d.args
  res = []
  list_of_args = all_configurations_args(args)
  for arg in list_of_args:
    new_def = copy.deepcopy(d)
    new_def.args = arg
    res.append(new_def)
    new_def2 = copy.deepcopy(new_def)
    new_def2.returns = None
    res.append(new_def2)
  else:
    return [res[0], res[-1]]

def branch(prefixes, suffixes):
  res = []
  if not prefixes:
    return [[s] for s in suffixes]
  for p in suffixes:
    for q in prefixes:
      res.append(q + [p])
  return res

counter_decorator = "counter"

def all_configurations_ast(tree):
  ast_copy = copy.deepcopy(tree)
  body = ast_copy.body
  ast_list = []
  body_list = []
  for node in body:
    if isinstance(node, ast.FunctionDef):
      node.decorator_list = [d for d in node.decorator_list if d.id == counter_decorator]
      body_list = branch(body_list, all_configurations_def(node))
    elif isinstance(node, ast.ClassDef):
      node_no_dec = copy.deepcopy(node)
      node_no_dec.decorator_list = []

      body_list1 = branch(body_list, all_configurations_ast(node))
      body_list2 = branch(body_list, all_configurations_ast(node_no_dec))
      body_list = body_list1 + body_list2
    else:
      body_list = branch(body_list, [node])
  for body in body_list:
    new_ast = copy.deepcopy(tree)
    new_ast.body = body
    ast_list.append(new_ast)
  return ast_list

def all_configurations(parsed, filename, output_directory):
  name = file_name(filename)
  if not os.path.exists(output_directory):
    os.mkdir(output_directory)
  file_directory = os.path.join(output_directory, name)
  if not os.path.exists(file_directory):
    os.mkdir(file_directory)
  all_configs = all_configurations_ast(parsed)
  i = 0
  for ast in all_configs:
    with open("%s/%s.py" % (file_directory, i), "w") as out:
      print(to_source(ast), file=out)
    i += 1
  return

def get_all_files(dir_path):
   return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

def gen_all(d):
  dir_path = "%s/%s" % (d, TYPED)
  target = "%s/%s" % (d, BENCHMARK)
  parsed = []
  n=None
  all_files = get_all_files(dir_path)
  for f in all_files:
      p = os.path.join(dir_path, f)
      parsed.append(parse_ast(p))
  print("Generating configurations for %s" % all_files)
  for i in range(len(parsed)):
    all_configurations(parsed[i], all_files[i], target)
  return

# -----------------------------------------------------------------------------
## main

def ensure_dir(d):
  if not os.path.exists(d):
    os.mkdir(d)
  return

def ensure_file(f):
  if not os.path.exists(f):
    open(f, "a").close()
  return

def is_benchmark(d):
  return os.path.isdir(d) and os.path.exists("%s/%s" % (d, TYPED))

def is_clean_benchmark(d):
  """
    Check if benchmark directory `d` has anything leftover from a past setup
    @returns Boolean
  """
  aliens = []
  for should_not_exist in [BENCHMARK, TEST, "karst*"]:
    aliens.extend(glob.glob("%s/%s" % (d, should_not_exist)))
  if bool(aliens):
    print("Benchmark directory %s has folders leftover from a previous setup:" % d)
    for alien in aliens:
      print("* %s" % alien)
    print("Remove these, then call './setup_karst.py %s'" % d)
    return False
  else:
    return True

def file_name(path):
  return os.path.splitext(os.path.basename(path))[0]

def test_typed_config(typed_dir, both_dir, test_dir):
  staging_dir = "%s/STAGING" % test_dir
  shutil.copytree(both_dir, staging_dir)
  for py in glob.iglob("%s/*.py" % typed_dir):
    shutil.copy(py, staging_dir)
  ok = False
  cmd = "%s %s/%s" % (RETIC, staging_dir, MAIN)
  try:
    out_time = float(str(subprocess.check_output(cmd, shell=True), encoding="utf-8"))
    ok = True
  except subprocess.CalledProcessError as cpe:
    print("Error running retic: %s" % cpe.message)
  except ValueError:
    print("Error running retic: output of %s was not (just) a float" % cmd)
  finally:
    shutil.rmtree(staging_dir)
    return ok

def run(dirs):
  for d in dirs:
    if not is_benchmark(d):
      continue
    if not is_clean_benchmark(d):
      continue
    print("Setting up '%s'" % d)
    # -- ok, really setup the benchmark
    both_dir = "%s/%s" % (d, BOTH)
    test_dir = "%s/%s" % (d, TEST)
    ensure_dir(both_dir)
    shutil.copyfile(TIMER, "%s/Timer.py" % both_dir)
    ensure_dir(test_dir)
    # -- check that typed config actually runs
    if not test_typed_config("%s/%s" % (d, TYPED), both_dir, test_dir):
      shutil.rmtree(test_dir)
      return
    gen_all(d)
    ensure_file("%s/%s" % (d, KARST_OUTPUT))
    all_config_files = [glob.iglob("%s/*" % d) for d in glob.glob("%s/%s/*/" % (d, BENCHMARK))]
    output_index = 1
    output_file  = open("%s/%s%s" % (d, KARST_INPUT, output_index), "w")
    lines_left   = LINES_PER_KARST_FILE
    for files in itertools.product(*all_config_files):
      print("-".join((file_name(x) for x in files)), file=output_file)
      lines_left -= 1
      if lines_left == 0:
        output_file.close()
        output_index += 1
        output_file  = open("%s/%s%s" % (d, KARST_INPUT, output_index), "w")
        lines_left   = LINES_PER_KARST_FILE

## -----------------------------------------------------------------------------

if __name__ == "__main__":
  # By default, run on all benchmark directories.
  # If directories are given, 
  if len(sys.argv) > 1:
    run([d for d in sys.argv[1::]
         if os.path.exists("%s/" % d)])
  else:
    run(glob.glob("%s/*/" % RP))
