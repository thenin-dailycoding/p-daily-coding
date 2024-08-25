import gc
import logging
from typing import Protocol, Sequence
import argparse
from dc_utils import timeitt

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger("TwoSum")


class Summable(Protocol):
    def __add__(self, value): ...


class Substractable(Summable, Protocol):
    def __sub__(self, value): ...


class Comparable(Summable, Protocol):
    def __gt__(self, value): ...
    def __lt__(self, value): ...


@timeitt(10)
def bruteforce[T: Summable](values: Sequence[T], target: T) -> bool:
    """
    Bruteforce solution
    Time complexity: O(n**2)
    """
    if len(values) < 2:
        raise ValueError(f"Invalid parameter length: {values}")

    for idx, left in enumerate(values):
        for right in values[idx:]:
            if left + right == target:
                return True
    return False


@timeitt(10)
def cashed_set[T: Substractable](values: Sequence[T], target: T) -> bool:
    """
    Using a set as a cache for items previousely rejected.
    If the differences between taget anmd next sequence item
    exists in the set, there is a pair of values which add up to target.

    Time complexity: O(n)
    Space compexity: O(n)
    """
    if len(values) < 2:
        raise ValueError(f"Invalid parameter length: {values}")

    # set contains the list of substitution result candidates
    remains = set()
    for value in values:
        if (target - value) in remains:
            return True
        remains.add(value)

    return False


@timeitt(10)
def binary_search[T: Comparable](values: Sequence[T], target: T) -> bool:
    """
    Assuming the sequence is sorted ASC
    """
    if len(values) < 2:
        raise ValueError(f"Invalid parameter length: {values}")
    left = 0
    right = len(values)-1
    while left < right:
        the_sum = values[left] + values[right]
        if the_sum == target:
            return True
        if the_sum > target:
            right -= 1
        else:
            left += 1

    return False


def main(argv: Sequence | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python "+__file__, description="TwoSum"
    )
    parser.add_argument("-l", "--length", default=10000, type=int,
                        help="array length, default = 1000")
    args = parser.parse_args(argv)

    methods = [cashed_set, bruteforce, binary_search]
    sequence = tuple(range(args.length))
    slices = (slice(-2, None),
              slice(None, 2),
              slice(length := len(sequence) >> 1, length+2),
              slice(length := len(sequence) >> 2, None, length*2),)

    pairs = tuple(sequence[item] for item in slices)
    tests = dict.fromkeys(pairs, methods)

    for key, value in tests.items():
        target = sum(key)
        logger.info(f"Length: {len(sequence)} | Indices: {key} | Target: {key[0]} + {key[1]} = {target}")  # noqa: E501
        for f in value:
            gc.collect()
            f(sequence, target)
        print()

    return 0


if __name__ == "__main__":
    exit(main())
