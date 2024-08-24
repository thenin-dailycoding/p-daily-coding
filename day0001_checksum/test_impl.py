import pytest
from .impl import bruteforce, checksum_not_subbable, checksum_subbable


@pytest.mark.parametrize(
    "input, target, expected",
    [
        ((1, 2, 3, 4, 5, 6, 7, 8, 9), 17, True),
        ((1, 2, 3, 4, 5, 6, 7, 8), 17, False),
        ([10, 15, 3, 7], 17, True),
        (("car", "cat", "dog", "pool", "42"), "carpool", True),
        (("car", "cat", "dog", "pool", "42"), "carpools", False),
    ]
)
def test_bruteforce(input, target, expected):
    assert bruteforce(input, target) == expected


@pytest.mark.parametrize(
    "input, target, expected",
    [
        ((1, 2, 3, 4, 5, 6, 7, 8, 9), 17, True),
        ((1, 2, 3, 4, 5, 6, 7, 8), 17, False),
        ([10, 15, 3, 7], 17, True),
        ([17, 0], 17, True),
        ([17, 1], 17, False),
    ]
)
def test_checksum_subbable(input, target, expected):
    assert checksum_subbable(input, target) == expected


@pytest.mark.parametrize(
    "input, target, expected",
    [
        ((1, 2, 3, 4, 5, 6, 7, 8, 9), 17, True),
        ((1, 2, 3, 4, 5, 6, 7, 8), 17, False),
        ([10, 15, 3, 7], 17, True),
        ([17, 0], 17, True),
        ([17, 1], 17, False),
        (("car", "cat", "dog", "pool", "42"), "carpool", True),
        (("car", "cat", "dog", "pool", "42"), "carpools", False),
    ]
)
def test_checksum_not_subbable(input, target, expected):
    assert checksum_not_subbable(sorted(input), target) == expected
