from pip import main
from python_problems.leetcode.roman_numerals.roman_to_int import Solution
import pytest


@pytest.mark.parametrize(
    "in_r_string,expect_n_list", [("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000])]
)
def test_roman_to_num_list(in_r_string, expect_n_list):
    roman_converter = Solution()

    n_list = roman_converter._roman_to_num_list(in_r_string)

    assert expect_n_list == n_list


@pytest.mark.parametrize(
    "in_num_list,out_num_list",
    [
        ([1, 5, 5, 1], [-1, 5, 5, 1]),
        ([5, 1], [5, 1]),
        ([1, 5, 10, 50], [-1, -5, -10, 50]),
    ],
)
def test_add_signs(in_num_list, out_num_list):
    roman_converter = Solution()

    n_list = roman_converter._add_signs_left_of_max(in_num_list)

    assert out_num_list == n_list


@pytest.mark.parametrize(
    "in_num_list,out_groups",
    [([1000, 100, 1000, 10, 100, 1, 5], [[1000], [100, 1000], [10, 100], [1, 5]])],
)
def test_get_groups(in_num_list, out_groups):
    roman_converter = Solution()

    groups = roman_converter._get_groups(in_num_list)

    assert out_groups == groups


@pytest.mark.parametrize(
    "in_roman,out_int", [("I", 1), ("IV", 4), ("IVXLCDM", 334), ("MCMXCIV", 1994)]
)
def test_romantoint(in_roman, out_int):
    roman_converter = Solution()

    n_list = roman_converter.romanToInt(in_roman)

    assert out_int == n_list
