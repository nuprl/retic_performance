import DirPaths

from Num import Num
from And import And
from If import If
from Boolean import Boolean
from Variable import Variable
from FuncDef import FuncDef
from FuncApplication import FuncApplication
from StructDef import StructDef
from LambdaExpr import LambdaExpr
from Parser import token_parser, exp_parser, func_def_parser,\
                   struct_def_parser, parse, parse_lambda
from ParserError import ParserError

import pytest


class Test_parser:
    """
    To represent Parser tests
    """

    def test_parse(self):
        assert parse(['+', 1, [1, '+']]) == \
               FuncApplication\
                   (Variable('+'),
                    [Num(1), FuncApplication(Num(1), [Variable('+')])])

        assert parse(['+', 1, 2]) == \
               FuncApplication(Variable('+'), [Num(1), Num(2)])
        assert parse(['define-struct', 'posn', ['x', 'y']]) ==\
               (StructDef('posn', ['x', 'y']))
        with pytest.raises(ParserError):
            parse(exp_parser([]))


    def test_token(self):
        assert token_parser(42) == Num(42)
        assert token_parser('x') == Variable('x')
        assert token_parser('+')  == Variable('+')

    def test_expr_parser(self):
        assert exp_parser(['+', 'a', 'b']) ==\
               FuncApplication(Variable('+'), [Variable('a'), Variable('b')])
        assert exp_parser([1]) == FuncApplication(Num(1), [])
        assert exp_parser([1, '+', 1]) == \
               FuncApplication(Num(1), [Variable('+'), Num(1)])

        with pytest.raises(ParserError):
            exp_parser('define')

        with pytest.raises(ParserError):
            exp_parser(['-'])

    def test_add_bsl_expr(self):
        assert exp_parser(['+']) == FuncApplication(Variable('+'), [])
        assert exp_parser(['+', 1]) == FuncApplication(Variable('+'),[Num(1)])
        assert exp_parser(['+', 1, 1]) == \
               FuncApplication(Variable('+'), [Num(1), Num(1)])
        assert exp_parser(['+', 1, '+', 1]) == \
               FuncApplication(Variable('+'), [Num(1), Variable('+'), Num(1)])

    def test_mult_bsl_expr(self):
        assert exp_parser(['*', 1, 1]) == \
               (FuncApplication(Variable('*'), [Num(1), Num(1)]))
        assert exp_parser(['*']) == (FuncApplication(Variable('*'), []))

    def test_subtract_bsl_expr(self):
        assert exp_parser(['-', 1, 1]) == \
               (FuncApplication(Variable('-'), [Num(1), Num(1)]))
        assert exp_parser(['-', 1,['-', 1]]) ==\
               (FuncApplication
                (Variable('-'),
                 [Num(1),
                  FuncApplication(Variable('-'), [Num(1)])]))
        assert exp_parser(['-', 1]) == \
               FuncApplication(Variable('-'), [Num(1)])

    def test_divide_bsl_expr(self):
        assert exp_parser(['/', 1, 1]) == \
               (FuncApplication(Variable('/'), [Num(1), Num(1)]))
        assert exp_parser(['/', 1,['-', 1]]) ==\
               (FuncApplication
                (Variable('/'),
                 [Num(1), FuncApplication(Variable('-'), [Num(1)])]))
        assert exp_parser(['/', 1]) == \
               (FuncApplication(Variable('/'), [Num(1)]))

    def test_composite_bsl_expr(self):
        assert exp_parser(['*', 1,['+', 1]]) == \
               (FuncApplication
                (Variable('*'),
                 [Num(1),
                  FuncApplication(Variable('+'), [Num(1)])]))

        assert exp_parser(['*', 1, ['-', 2, 2], ['/', 1]]) == \
               (FuncApplication
                (Variable('*'),
                 [Num(1),
                  FuncApplication(Variable('-'), [Num(2),Num(2)]),
                  FuncApplication(Variable('/'), [Num(1)])]))

    def test_function_definition(self):

        assert func_def_parser\
                   (['define', ['add', 'x', 'y', 'z'], ['+', 1, 3]]) == \
               FuncDef\
                   ('add',
                    LambdaExpr(['x', 'y', 'z'],
                    FuncApplication(Variable('+'),
                    [Num(1), Num(3)])))

        assert func_def_parser(['define', 'add', ['+', 1, 3]]) == \
               FuncDef('add', FuncApplication(Variable('+'), [Num(1), Num(3)]))

    def test_struct_definition(self):

        assert struct_def_parser(['define-struct', 'posn', ['x', 'y']]) == \
               (StructDef('posn', ['x', 'y']))
        assert struct_def_parser(['define-struct', 'add', ['x', 'y', 'z']]) == \
               StructDef('add', ['x', 'y', 'z'])

    def test_not_struct_def(self):
        with pytest.raises(ParserError):
            struct_def_parser(['define-struct', 'posn', [1, 2, 3]])

        with pytest.raises(ParserError):
            struct_def_parser(['define-struct', 1, []])

    def test_not_function_definition(self):

        with pytest.raises(ParserError):
            func_def_parser(['define', ['f', 'x', 1, 'y'], 42])

        with pytest.raises(ParserError):
            func_def_parser(['define'])
            func_def_parser(['define', 'add'])
            func_def_parser(['define', ['+', 1, 3]])
            func_def_parser(['define', ['Add', '+', 'y', 'z'], ['+', 1, 3]])
        assert not func_def_parser(['a', ['add', 'x', 'y', 'z'], ['+', '+', 3]])

    def test_function_application(self):

        assert exp_parser(['f', 1]) == \
               (FuncApplication(Variable('f'), [Num(1)]))

        assert exp_parser(['f', 1, 2]).__eq__\
            (FuncApplication(Variable('f'), [Num(1), Num(2)]))
        assert exp_parser(['x',1]).__eq__\
            (FuncApplication(Variable('x'),[Num(1)]))

        assert not exp_parser(['define',['x',1],1])

    def test_and(self):
        assert exp_parser(['and', 'true', 'true']) == \
               And([Boolean(True), Boolean(True)])

    def test_equals(self):
        assert exp_parser(['=', 3, 3]) ==\
               FuncApplication(Variable('='), [Num(3), Num(3)])

        with pytest.raises(ParserError):
            exp_parser(['=', 3])

    def test_bigger_less_than(self):
        assert exp_parser(['>', 3, 3]) == \
               FuncApplication(Variable('>'), [Num(3), Num(3)])

        with pytest.raises(ParserError):
            exp_parser(['>', 3])

    def test_exponent(self):
        assert exp_parser(['^', 2, 3]) ==\
               FuncApplication(Variable('^'),[Num(2), Num(3)])

    def test_if(self):
        assert exp_parser(['if', 1 , 'true', 'false']) == \
               If([Num(1), Boolean(True), Boolean(False)])

        assert exp_parser(['if', 'false', ['/', 1, 0], 9]) == \
               If([Boolean(False),
                   FuncApplication(Variable('/'), [Num(1), Num(0)]),
                   Num(9)])

    def test_lambda(self):
        assert parse_lambda(['lambda', ['x'], 'x']) == \
               LambdaExpr(['x'], Variable('x'))
