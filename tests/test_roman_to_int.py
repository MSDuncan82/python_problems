from leetcode.roman_numerals import RomanToInteger
import pytest


@pytest.mark.parametrize("in_r_string,expect_n_list", ['IVXLCDM', [1, 5, 10, 50, 100, 500, 1000]])
def test_roman_to_num_list(in_r_string, expect_n_list):
    roman_converter = RomanToInteger()

    n_list = roman_converter.roman_to_num_list(in_r_string)

    assert expect_n_list == n_list
    
