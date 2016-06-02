import pytest
from Untyped.Utilities import relative_average, accumulated_s

def test_relative_average():
    assert relative_average([1, 2, 3], 1) == 2
    assert relative_average([1, 2, 3], 2) == 1

def test_accumulated_s():
    assert accumulated_s([1]) == [1]
    assert accumulated_s([2, 2]) == [.5, 1]
    assert accumulated_s([2, 8]) == [.2, 1]

