import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from math_functions import square, factorial, is_prime, gcd, lcm

def test_square():
    assert square(2) == 4
    assert square(-3) == 9

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(4) is False
    assert is_prime(1) is False

def test_gcd():
    assert gcd(54, 24) == 6
    assert gcd(10, 0) == 10

def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(0, 5) == 0
