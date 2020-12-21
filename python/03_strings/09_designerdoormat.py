# Solution to [Designer Door Mat](https://www.hackerrank.com/challenges/designer-door-mat)


##########
# Constants
##########

msg = "WELCOME"
dash = '-'
design = ".|."


##########
# Imports
##########

from typing import Tuple


##########
# Input
##########

def get_input() -> Tuple[int, int]:
    """Returns N x M integer input for Designer Doormat.

    Returns:
        Tuple[int, int]: N x M, representing length & width.
    """
    n, m = [int(x) for x in input().split()]
    if n % 2 == 0: 
        raise Exception("Not odd!")
    if m != 3* n:
        raise Exception("M must be 3n!")
    return n, m


##########
# Print lines
##########

def get_dashes(num_dashes: int) -> str:
    """Returns dashes from number of dashes"""
    return num_dashes * dash


def print_welcome(m: int) -> None:
    """Prints welcome message."""
    
    num_dashes = (m - len(msg)) // 2
    dashes = get_dashes(num_dashes)

    print(dashes, msg, dashes, sep = '')
    return


def print_design(row: int, m: int) -> None:
    """Prints design for rows without welcome message

    Args:
        row (int): Row number (from mid)
        m (int): length of row
    """
    row_design = design * (row * 2 + 1)
    num_dashes = (m - len(row_design)) // 2
    dashes = get_dashes(num_dashes)

    print(dashes,row_design, dashes, sep = '')
    return


def print_line(row: int, n: int, m: int) -> None:
    """Prints line for door mat.

    Args:
        row (int): row number
        n (int): length
        m (int): width
    """
    mid = (n-1) // 2

    ## Middle row
    if row == mid:
        print_welcome(m)
        return
    
    ## Account for inverted design
    if row > mid:
        row = mid - (row - mid)
    
    print_design(row, m)
    return


##########
# Main
##########

if __name__ == "__main__":
    n, m = get_input()

    for i in range(0, n):
        print_line(i, n, m)

