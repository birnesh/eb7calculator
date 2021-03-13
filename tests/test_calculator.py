import pytest
from eb7calculator import calculator as calc

def test_add():
    """ Test that checks the functionality of add() function"""
    input_a = 1
    input_b = 2
    assert calc.add(input_a, input_b) == 3

def test_sub():
    """ Test that checks the functionality of sub() function"""
    input_a = 3
    input_b = 1
    assert calc.sub(input_a, input_b) == 2

def test_mul():
    """ Test that checks the functionality of mul() function"""
    input_a = 10
    input_b = 2
    assert calc.mul(input_a, input_b) == 20

def test_div():
    """ Test that checks the functionality of div() function"""
    input_a = 10
    input_b = 2
    assert calc.div(input_a, input_b) == 5.0
    assert type(calc.div(input_a, input_b)) != type(5)
 
