import pytest
from contextlib import nullcontext as does_not_raise
from impl import bruteforce, cashed_set, binary_search


@pytest.mark.parametrize(
    "input, target, expected",
    [
        ((1, 2, 3, 4, 5, 6, 7, 8, 9), 17, True),
        ((1, 2, 3, 4, 5, 6, 7, 8), 17, False),
        ([10, 15, 3, 7], 17, True),
        (((0, 1), (2, 3), (4, 5, 6), (7, 8)), (0, 1, 7, 8), True),
        (((0, 1), (2, 3), (4, 5, 6), (7, 8)), (0, 1, 6, 8), False),
    ]
)
def test_bruteforce(input, target, expected):
    assert bruteforce(input, target) == expected


@pytest.mark.parametrize(
    "input, target, expected, expectation",
    [
        ((1, 2, 3, 4, 5, 6, 7, 8, 9), 17, True, does_not_raise()),
        ((1, 2, 3, 4, 5, 6, 7, 8), 17, False, does_not_raise()),
        ([10, 15, 3, 7], 17, True, does_not_raise()),
        ([17, 0], 17, True, does_not_raise()),
        ([17, 1], 17, False, does_not_raise()),
        (((0, 1), (2, 3), (4, 5, 6), (7, 8)),
         (0, 1, 7, 8), None, pytest.raises(TypeError)),
        (((0, 1), (2, 3), (4, 5, 6), (7, 8)),
         (0, 1, 6, 8), None, pytest.raises(TypeError)),
    ]
)
def test_checksum_subbable(input, target, expected, expectation):
    with expectation:
        assert cashed_set(input, target) == expected


@pytest.mark.parametrize(
    "input, target, expected",
    [
        ((1, 2, 3, 4, 5, 6, 7, 8, 9), 17, True),
        ((1, 2, 3, 4, 5, 6, 7, 8), 17, False),
        ([10, 15, 3, 7], 17, True),
        ([17, 0], 17, True),
        ([17, 1], 17, False),
        (((0, 1), (2, 3), (4, 5, 6), (7, 8)), (0, 1, 7, 8), True),
        (((0, 1), (2, 3), (4, 5, 6), (7, 8)), (0, 1, 6, 8), False),
    ]
)
def test_checksum_not_subbable(input, target, expected):
    assert binary_search(sorted(input), target) == expected
