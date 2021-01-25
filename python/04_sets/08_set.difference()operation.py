# Solution to [Set .difference() Operation](https://www.hackerrank.com/challenges/py-set-difference-operation/problem)

##########
# Imports
##########

from typing import Tuple, Set


##########
# Input
##########

def get_inputs() -> Tuple[Set[int]]:
    """Returns two lists of integers

    Returns:
        Tuple[Set[int]]: 2 lists of ints
    """
    _ = input()
    english_class = set(map(int, input().split()))
    _ = input()
    french_class = set(map(int, input().split()))
    return english_class, french_class


##########
# Main
##########
def main():
    english_class, french_class = get_inputs()
    english_only = english_class.difference(french_class)
    print(len(english_only))


if __name__ == "__main__":
    main()