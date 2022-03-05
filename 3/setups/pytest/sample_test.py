import pytest

from sample import func, divisor

def testFunc():
    assert func(-1) == 0
    assert func(2) == 3
    assert func(3) == 4

def assertDivisor():
    assert divisor(12) == 1
    assert divisor(6) == 2
    assert divisor(3) == 3


def assertDivisorException():
     with pytest.raises(ZeroDivisionError):
        divisor(0)