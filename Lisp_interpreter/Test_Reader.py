from Reader import Reader

reader1 = Reader("1234")
reader2 = Reader("1234")
reader3 = Reader("12 4")
reader4 = Reader("123")
reader5 = Reader("123")
read_mt = Reader("()")
read_f10 = Reader('(f 10)')
read_f_of_g10 = Reader('(f(g 10))')
read_blank_old = Reader('(  f(g))')
read_blank = Reader('(   token0(token1))')
read_function_definition = Reader('(define (add x y z) (+ 1 3))')
read_function_definition_no_params = Reader('(define add (+ 1 3))')

class Test_Reader:

    def test_reader(self):

        assert reader1.read_char() == "1"
        assert reader2.read_first_proper_char() == "1"

        assert reader1.read_token_acc(['g','x']) == ['xg234', '']
        assert reader3.read_token_acc(['g', 'x']) == ['xg12', " "]

        assert reader4.read_token(['1']) == [1123, '']

        assert reader5.reader() == 123

        assert read_mt.reader() == []
        assert read_f10.reader() == ["f", 10]
        assert read_f_of_g10.reader() == ["f",["g",10]]

        assert read_blank.reader() == ["token0", ["token1"]]

        assert read_function_definition.reader() == ['define', ['add', 'x', 'y', 'z'], ['+', 1, 3]]
        assert read_function_definition_no_params.reader() == ['define', 'add', ['+', 1, 3]]


