# Solution to [Set .discard(), .remove() & .pop()](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem)

from typing import Set


def get_input() -> Set[int]:
    """Returns set of integers in s.

    Returns:
        List[int]: s, set of integers.
    """
    _ = input()
    s = set( map(int, input().split()))
    return s


def main():
    s = get_input()
    n = int(input())

    for _ in range(n):
        info = input().split()
        if len(info) == 1:
            info.append('')     # can pop w/o an element

        cmd, num = info
        eval(f"s.{cmd}({num})")

    print( sum(s))


if __name__ == "__main__":  
    main()
