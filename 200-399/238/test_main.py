import pytest
from main import Solution


@pytest.mark.parametrize(
    "in_data, expected_data",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([0, 0], [0, 0]),
    ],
)
def test_main(in_data, expected_data):
    assert Solution().productExceptSelf(in_data) == expected_data
