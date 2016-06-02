from Test_Automata import defects, cooperates, tit_for_tat, grim_trigger
from Untyped.Population import Population

a1 = [defects(0), cooperates(0)]
p1 = Population(a1)
e1 = [defects(40), cooperates(0)]
p1_expected = Population(e1 + a1)

a2 = [defects(0), tit_for_tat(0)]
p2 = Population(a2 + a2)
e2 = [defects(13), tit_for_tat(9)]
p2_expected = e2 + a2

a3 = [tit_for_tat(0), defects(0)]
p3 = a3 + a3
e3 = [tit_for_tat(9), defects(13)]
p3_expected = Population(e3 + a3)


#Doesn't work due to changing population
def test_population():
    assert p2.match_up(10)


a = cooperates(1)
p = Population([a, a])

def test_regenerate():
    assert p.regenerate(1) == p

a20 = [cooperates(1), cooperates(9)]
p20 = Population(a20)

c0 = cooperates(0)
c9 = cooperates(9)


# #Need to verify that this test is written correctly
# def test_regenerate2():
#
#     def f(p):
#         a = p.a
#         return (a[0] == c0 and a[1] == c9) or (a[0] == c9 and a[1] == c0)
#     assert not f(p20.regenerate(1, .2))