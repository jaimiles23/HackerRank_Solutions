# Solution to [Symmetric Difference](https://www.hackerrank.com/challenges/symmetric-difference)

from typing import Tuple, Set

def get_input() -> Tuple[Set[int]]:
    """Returns M and N sets of integers.

    Returns:
        Tuple[Set[int]]: Set M of ints, Set N of ints
    """
    _ = input()
    m = set(map(int, input().split()))
    _ = input()
    n = set(map(int, input().split()))
    return m, n


def main():
    m, n = get_input()

    m_only = m.difference(n)
    n_only = n.difference(m)
    disparate_ints = m_only.union(n_only)
    disparate_ints = sorted(list(disparate_ints))
    for elem in disparate_ints:
        print(elem)


if __name__ == "__main__":
    main()