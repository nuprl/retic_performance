# Usage:
#    python remove_types.py <dir>
# where `<dir>` is a benchmark directory
#
# Creates a directory <dir>_untyped and saves a runnable, fully-untyped
#  copy of the given benchmark to it.
#
# To run the generated code:
# - cd <dir>_untyped
# - python main.py
#
# (Generated code should run via python or retic)

## -----------------------------------------------------------------------------
## imports

import ast
import copy
import glob
import os
import shutil
import subprocess
import sys

## -----------------------------------------------------------------------------
## constants

BOTH      = "both"
TYPED     = "typed"

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

def remove_types_args(typed_args):
  new_args = copy.deepcopy(typed_args)
  for j in range(len(typed_args.args)):
    new_args.args[j].annotation = None
  return new_args

counter_decorator = "counter"

def remove_types_def(d):
  args = d.args
  new_args = remove_types_args(args)
  new_def = copy.deepcopy(d)
  new_def.args = new_args
  new_def.returns = None
  return new_def

def remove_types_ast(tree):
  ast_copy = copy.deepcopy(tree)
  body = ast_copy.body
  new_body = []
  for node in body:
    if isinstance(node, ast.FunctionDef):
      node.decorator_list = [d for d in node.decorator_list if d.id == counter_decorator]
      new_body.append(remove_types_def(node))
    elif isinstance(node, ast.ClassDef):
      node_no_dec = copy.deepcopy(node)
      node_no_dec.decorator_list = []
      new_body.append(remove_types_ast(node_no_dec))
    else:
      new_body.append(node)
  new_ast = copy.deepcopy(tree)
  new_ast.body = new_body
  return new_ast

def remove_types(parsed, filename, output_directory):
  name = file_name(filename)
  ast = remove_types_ast(parsed)
  with open("%s/%s" % (output_directory, filename), "w") as out:
    print(to_source(ast), file=out)
  return

def get_all_files(dir_path):
   return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

def gen_untyped(d, u_dir):
  both_dir = "%s/%s" % (d, BOTH)
  if os.path.exists(both_dir):
    for fn in glob.glob("%s/*.*" % both_dir):
      shutil.copyfile(fn, "%s/%s" % (u_dir, os.path.basename(fn)))
  dir_path = "%s/%s" % (d, TYPED)
  all_files = get_all_files(dir_path)
  parsed = [parse_ast(os.path.join(dir_path, f))
            for f in all_files]
  for i in range(len(parsed)):
    remove_types(parsed[i], all_files[i], u_dir)
  return

# -----------------------------------------------------------------------------
## main

def file_name(path):
  return os.path.splitext(os.path.basename(path))[0]

def is_benchmark(d):
  return os.path.isdir(d) and os.path.exists("%s/%s" % (d, TYPED))

def add_suffix(d, suffix):
  prefix = d
  if d.endswith("/"):
    prefix = prefix[:-1]
  return prefix + suffix

def run(d):
  if not is_benchmark(d):
    print("Error: %s is not a benchmark" % d)
    print_usage()
    return
  u_dir = add_suffix(d, "_untyped")
  print("Saving untyped version of %s to %s ..." % (d, u_dir))
  if os.path.exists(u_dir):
    print("Error: directory %s already exists" % u_dir)
    print_usage()
    return
  os.mkdir(u_dir)
  gen_untyped(d, u_dir)
  print("Done!")
  return

def print_usage():
  print("usage: python remove_types.py <BENCHMARK-FOLDER>") 
  return

def run_all(ds):
  for d in ds:
    run(d)

## -----------------------------------------------------------------------------

if __name__ == "__main__":
  # By default, run on all benchmark directories.
  # If directories are given, 
  if len(sys.argv) > 1:
    run_all(sys.argv[1:])
  else:
    print_usage()

