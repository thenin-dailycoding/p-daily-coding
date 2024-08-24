from typing import Sequence


def bruteforce(values: Sequence, target: object) -> bool:
    """
    Bruteforce solution
    Time complexity: O(n**2)
    Memory compexity: O(1)

    Args:
        values (Sequence): Sequence of valies to analyze
        target (object): Target sum

    Raises:
        ValueError: If the suplied sequence has less than 2 items

    Returns:
        bool: True if there is a pair of values, whic add up to target
    """
    if len(values) < 2:
        raise ValueError(f"Invalid parameter length: {values}")

    for idx, left in enumerate(values):
        for right in values[idx:]:
            if left + right == target:
                return True
    return False


def checksum_subbable(values: Sequence, target: object) -> bool:
    """
    Using a set as a cache
    Time complexity: O(n)
    Memory compexity: O(n)

    Args:
        values (Sequence): Sequence of valies to analyze
        target (object): Target sum

    Raises:
        ValueError: If the suplied sequence has less than 2 items

    Returns:
        bool: True if there is a pair of values, whic add up to target
    """
    if len(values) < 2:
        raise ValueError(f"Invalid parameter length: {values}")

    # set contains the list of sunstitution result candidates
    remains = set()
    for value in values:
        if (target - value) in remains:
            return True
        remains.add(value)

    return False


def checksum_not_subbable(values: Sequence, target: object) -> bool:
    """
    Implementation without substraction.
    Assumes incoming sequence is sorted ASC

    Args:
        values (Sequence): Sequence of valies to analyze
        target (object): Target sum

    Raises:
        ValueError: If the suplied sequence has less than 2 items

    Returns:
        bool: True if there is a pair of values, whic add up to target
    """
    if len(values) < 2:
        raise ValueError(f"Invalid parameter length: {values}")

    idx_left = 0
    idx_right = 1

    # if two smallest values are larger than target, exit the loop
    while ((idx_left < len(values)-1)
            and values[idx_left] + values[idx_left + 1] <= target):

        if (idx_right < len(values) and
                values[idx_left] + values[idx_right] == target):
            return True

        if (idx_right < len(values) and
                values[idx_left] + values[idx_right] < target):
            idx_right += 1
            continue
        idx_left += 1
        idx_right = idx_left + 1

    return False


def main(argv: Sequence | None = None) -> int:
    return 0


if __name__ == "__main__":
    exit(main())
