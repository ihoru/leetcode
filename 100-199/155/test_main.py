import pytest

from main import Solution


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("", ""),
        ("a", "a"),
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
    ],
)
def test_main(input_str, expected_output):
    assert Solution().reverseWords(input_str) == expected_output
