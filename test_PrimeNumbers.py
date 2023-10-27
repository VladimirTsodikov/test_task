import PrimeNumbers as pn
import pytest


def test_correct_prime_list():
    assert pn.prime_numbers(0, 10) == [2, 3, 5, 7]
    assert pn.prime_numbers(19, 29) == [19, 23, 29]
    assert pn.prime_numbers(90, 105) == [97, 101, 103]
    assert pn.prime_numbers(32, 36) == []
    assert pn.prime_numbers(2, 2) == [2]


def test_negative_border():
    assert pn.prime_numbers(-10, 5) == pn.prime_numbers(0, 5)
    assert pn.prime_numbers(-10, 5) == [2, 3, 5]
    assert pn.prime_numbers(-5, 0) == []
    assert pn.prime_numbers(-20, -3) == []


def test_float_border():
    assert pn.prime_numbers(0.5, 4.9999) == [2, 3]
    assert pn.prime_numbers(18.7, 29.9) == [19, 23, 29]
    assert pn.prime_numbers(19.00001, 29.4) == [23, 29]
    assert pn.prime_numbers(2.0, 2.0) == [2]
    assert pn.prime_numbers(-5.7, 3.6) == [2, 3]
    assert pn.prime_numbers(-89, -15.0) == []


def test_low_more_high():
    assert pn.prime_numbers(5, 2) == []
    assert pn.prime_numbers(8.1, 7.2) == []
    assert pn.prime_numbers(-1, -4) == []


def test_exception():
    with pytest.raises(TypeError):
        assert pn.prime_numbers('3', 18)
        assert pn.prime_numbers(3, '18')
        assert pn.prime_numbers([3], [18])
