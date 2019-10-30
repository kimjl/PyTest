#Import what we want to test
import mathlib

#Creating unit tests
#Must use the test_ prefix
#Execute in command line using py.test or python -m pytest
#py.test -v will give us the result of whether each test has passed or not
def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == 9

def test_calc_multiply():
    result = mathlib.calc_multiply(10, 4)
    assert result == 40
