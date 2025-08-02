import pytest

from main import Solution


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("", ""),
        ("a", "a"),
        ("B", "B"),
        ("ae", "ea"),
        ("bcd", "bcd"),
        ("abc", "abc"),
        ("aby", "aby"),
        ("abe", "eba"),
        ("hello", "holle"),
        ("aeiou", "uoiea"),
        ("AEIOU", "UOIEA"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),
        ("zxcae", "zxcea"),
        ("aeiouAEIOU", "UOIEAuoiea"),
        ("aeiouAEIOU-", "UOIEAuoiea-"),
    ],
)
def test_main(input_str, expected_output):
    assert Solution().reverseVowels(input_str) == expected_output
