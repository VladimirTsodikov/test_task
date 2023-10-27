import RomanNumeralsConvert as rnc
import pytest


def test_correct_convert():
    assert rnc.roman_numerals_to_int('I') == 1
    assert rnc.roman_numerals_to_int('IV') == 4
    assert rnc.roman_numerals_to_int('XIII') == 13
    assert rnc.roman_numerals_to_int('XIX') == 19
    assert rnc.roman_numerals_to_int('XXXIV') == 34
    assert rnc.roman_numerals_to_int('XLIX') == 49
    assert rnc.roman_numerals_to_int('LXXIV') == 74
    assert rnc.roman_numerals_to_int('XCIX') == 99
    assert rnc.roman_numerals_to_int('CXXII') == 122
    assert rnc.roman_numerals_to_int('CDLVIII') == 458
    assert rnc.roman_numerals_to_int('DCXXXVI') == 636
    assert rnc.roman_numerals_to_int('CMXCIX') == 999
    assert rnc.roman_numerals_to_int('MMXXIII') == 2023
    assert rnc.roman_numerals_to_int('MMMCDLVI') == 3456
    assert rnc.roman_numerals_to_int('MMMDCCCXC') == 3890
    assert rnc.roman_numerals_to_int('MMMCMXCIX') == 3999


def test_uncorrect_input():
    assert rnc.roman_numerals_to_int('1') is None
    assert rnc.roman_numerals_to_int('IVW') is None


def test_exception():
    with pytest.raises(TypeError):
        assert rnc.roman_numerals_to_int(1)
        assert rnc.roman_numerals_to_int(['I', 'V'])
