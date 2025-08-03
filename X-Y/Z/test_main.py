import pytest

from main import Solution


@pytest.mark.parametrize(
    "in_data, expected_data",
    [
        ("", ""),
    ],
)
def test_main(in_data, expected_data):
    assert Solution().XXX(in_data) == expected_data
