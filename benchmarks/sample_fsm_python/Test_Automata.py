import pytest
from Untyped.Automata import Automaton
from Untyped.Other import make_random_automaton

COOPERATE = 0
DEFECT = 1

t1 = [[1, 1],
      [1, 1]]
def defects(p0):
    return Automaton(DEFECT, p0, t1, DEFECT)

t2 = [[0, 0],
      [0, 0]]
def cooperates(p0):
    return Automaton(COOPERATE, p0, t2, COOPERATE)

t3 = [[0, 1],
      [0, 1]]
def tit_for_tat(p0):
    return Automaton(COOPERATE, p0, t3, COOPERATE)

t4 = [[0, 1],
      [1, 1]]
def grim_trigger(p0):
    return Automaton(COOPERATE, p0, t4, COOPERATE)

def test_automata1():
    result = defects(0).interact(cooperates(0), 10)
    assert result[0].payoff == 40
    assert result[1].payoff == 0

def test_automata2():
    result = defects(0).interact(tit_for_tat(0), 10)
    assert result[0].payoff == 13
    assert result[1].payoff == 9

def test_automata3():
    result = tit_for_tat(0).interact(defects(0), 10)
    assert result[0].payoff == 9
    assert result[1].payoff == 13

def test_make_random_automaton():
    assert isinstance(make_random_automaton(3), Automaton)

