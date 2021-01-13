# Solution to [Set .union() Operation](https://www.hackerrank.com/challenges/py-set-union)

from typing import Tuple, Set

def get_input() -> Tuple[Set[int]]:
    """Returns tuple of set of integers..

    Returns:
        Tuple[Set[int]]: Represent students w/ English & French magazine descriptions
    """
    _ = input()
    eng_students = set(s for s in input().split())
    _ = input()
    fr_students = set(s for s in input().split())
    return eng_students, fr_students


def main():
    eng_studs, fr_studs = get_input()
    at_least_one_sub = eng_studs.union(fr_studs)
    print(len(at_least_one_sub))


if __name__ == "__main__":
    main()