# Solution to [Set .intersection() Operation](https://www.hackerrank.com/challenges/py-set-intersection-operation)

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
    both_classes = english_class.intersection(french_class)
    print(len(both_classes))


if __name__ == "__main__":
    main()