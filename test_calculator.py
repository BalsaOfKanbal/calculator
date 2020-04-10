import pytest
import .calculator

def test_add():
    answer = calculator.add(1, 2)
    assert answer == 3
def test_subtract():
    answer = calculator.subtract(3, 1)
    assert answer == 2
def test_multiply():
    answer = calculator.multiply(5, 5)
    assert answer == 25
def test_divide():
    answer = calculator.divide(35, 7)
    assert answer == 5