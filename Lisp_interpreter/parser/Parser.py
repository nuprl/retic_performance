import DirPaths
import sys
sys.path.insert(0, '/Users/zeinamigeed/Lisp_interpreter/interpreter/BSL_Expr')

from Num import Num
from Boolean import Boolean
from And import And
from If import If
from Variable import Variable
from FuncDef import FuncDef
from FuncApplication import FuncApplication
from LambdaExpr import LambdaExpr
from StructDef import StructDef
from ParserError import ParserError

def parse(p):
    """
    Parses p
    :param p: p-expression
    :param s: current scope
    :return: AST
    """
    exp = exp_parser(p)
    if exp:
        return exp

    func_def = func_def_parser(p)
    if func_def:
        return func_def

    struct_def = struct_def_parser(p)
    if struct_def_parser(p):
        return struct_def

    else:
        raise ParserError('Wrong Expression')

def token_parser(p):
    """
    Parses tokens
    :param p: p-expression
    :return: AST
    """
    if isinstance(p, (complex, int, float)):
        return Num(p)

    elif isinstance(p, str):
        if p == 'true':
            return Boolean(True)
        elif p == 'false':
            return Boolean(False)

        elif is_reserved(p):
            raise ParserError('This word is reserved')
        else:
            return Variable(p)
    else:
        return False


def exp_parser(p):
    """
    Parses expressions
    :param p: List
    :return AST
    """

    #try to parse as a token
    token = token_parser(p)
    if token:
        return token
    elif p == []:
        raise ParserError('Expected a function after open paren but found nothing.')

    # now we know it is a parenthesize P-expression
    if p[0] == '+':
        return parse_operation(p, 0)

    elif p[0] == '*':
        return parse_operation(p, 0)

    elif p[0] == '-':
        return parse_operation(p, 1)

    elif p[0] == '/':
        return parse_operation(p, 1)

    elif p[0] == '=':
        return parse_operation(p, 2)

    elif p[0] == '>':
        return parse_operation(p, 2)

    elif p[0] == '<':
        return parse_operation(p, 2)

    elif p[0] == '^':
        return parse_operation(p, 2)

    elif p[0] == 'and':
        return parse_operation(p, 2, And)

    elif p[0] == 'if':
        return parse_operation(p, 3, If)

    elif p[0] == 'lambda':
        return parse_lambda(p)

    elif not is_reserved(p[0]):
        return parse_operation(p, 0)

    else:
        return False

def parse_lambda(p):
    if len(p) != 3:
        raise ParserError('Lambda expr error')

    else:
        list_of_params = parse_params(p[1])
        body = exp_parser(p[2])
        return LambdaExpr(list_of_params, body)



def struct_def_parser(p):
    """
    Parses Struct Definitions
    :param p: P-expression
    :return: StructDefinition
    """
    if p[0] != 'define-struct':
        return False

    elif len(p) != 3:
        raise ParserError('length of p-expression must have length >= 3')

    elif not isinstance(p[1], str):
        raise ParserError('Struct name must be a string')

    elif is_reserved(p[1]):
        raise ParserError('Struct name is a reserved word')

    elif not isinstance(p[2], list):
        raise ParserError('Expects a list of parameters')

    elif not is_list_of_proper_names(p[2]):
        raise ParserError('Not a proper list of field names')

    else:
        return StructDef(p[1], p[2])

def func_def_parser(p):
    """
    Parses Function Definitions ['define',[f x ...], p-body]
    generates BSL_Def f is bound to (lambda (x ...) exp-body)
    :param p: P-expression
    :return: FuncDefinition
    """
    if p[0] != 'define':
        return False

    elif len(p) != 3:
        raise ParserError('p-expression must have length >= 3')

    elif isinstance(p[1], str):
        #Here, we know it is a constant
        if is_reserved(p[1]):
            raise ParserError('Variable cannot be a reserved word')
        else:
            # deals with (define x 3)
            # deals with (define x (lambda (y) y))
            name = p[1]
            rhs = exp_parser(p[2])
            return FuncDef(name, rhs)
    else:
        # deals with (define (f x ...) e)
        # as if it were (define f (lambda (x ...) e))
        lst = parse_params(p[1])
        name = lst[0]
        rhs = LambdaExpr (lst[1:], exp_parser(p[2]))
        return FuncDef(name, rhs)


def is_list_of_proper_names(expr):
    """
    Checks that expr is a list of strings and that no string is a reserved string
    :param expr: [string]
    :return: True/False
    """
    if not is_string_list(expr):
        return False
    elif not contains_reserved_words(expr):
        return False
    else:
        return True

def is_string_list(a_list):
    """
    Checks that every element is a string
    :param a_list: []
    :return: True if list of strings and False otherwise
    """
    for element in a_list:
        if not isinstance(element, str):
            return False

    return True


def contains_reserved_words(expr):
    """
    Checkes if any of the reseved words are in the parameter list
    :param expr: [string]
    :return: True if no reserved words are used and False otherwise
    """
    for element in expr:
        if is_reserved(element):
            return False
    return True

def is_reserved(word):
    """
    Determines if word is reserved
    :param word: String representing the variable
    :return: True if word is reserved and False otherwise
    """
    lorw = ['define','define-struct']
    return word in lorw


def parse_operation(p, n, expr=None):
    """
    Parses Operation that needs at least n arguments
    :param p: p-expresson
    :param n: Number of args
    :param lang: language used to parse
    :param expr: if this is an expr, not a function application, set this value to the class
    :return: FuncApplication or BSLExpr
    """
    name = exp_parser(p.pop(0))

    if len(p) < n:
        raise ParserError('expects at least %s argument, but found none' % str(n))
    else:
        result = parse_expr_list(p)

    if expr:
        return expr(result)

    return FuncApplication(name, result)


def parse_expr_list(lst):
    """
    Parses a list of expressions
    :param lst: List of P-expressions
    :return: List of BSLExpr
    """
    result = []
    for element in lst:
        element_as_bsl_exp = exp_parser(element)
        if not element_as_bsl_exp:
            raise ParserError('expects s-expressions in the list of arguments')
        result.append(element_as_bsl_exp)
    return result


def parse_params(a_list):
    """
    :param a_list: Some list
    """
    if isinstance(a_list, list):
        lst = a_list #name and params
        if not is_list_of_proper_names(lst):
            raise ParserError('All names must be strings')
    return a_list
