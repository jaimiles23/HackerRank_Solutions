# Solution to [No Idea!](https://www.hackerrank.com/challenges/no-idea)
from typing import Tuple


def get_input() -> Tuple[int, int, list, set, set]:
    """Returns input for challenge "No Idea!

    Returns:
        Tuple[int, int, list, set, set]: n, m, array, A, B
    """
    n, m = (int(x) for x in input().split())
    arr = input().split()
    a = set(input().split())
    b = set(input().split())

    return n, m, arr, a, b


def main():
    _, _, arr, happy_set, sad_set = get_input()
    ## NOTE: Because arr can have duplicates, cannot use set math.
    happy_score = sum([(i in happy_set) for i in arr])
    sad_score = sum([(i in sad_set) for i in arr])

    print(happy_score - sad_score)


if __name__ == "__main__":
    main()









