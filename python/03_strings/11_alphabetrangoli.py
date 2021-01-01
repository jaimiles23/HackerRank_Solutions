# Solution to [Alphabet Rangoli](https://www.hackerrank.com/challenges/alphabet-rangoli)

##########
# Constants
##########

RANGOLI_SPACING = '-'   # b/w chars
RANGOLI_START = 97      # starts @ 'a'


##########
# Size functions
##########

def get_height(n: int) -> int:
    """Returns height of rangoli."""
    return 2*n - 1


def get_width(n: int) -> int:
    """Returns width of rangoli."""
    if n == 1:  # basecase
        return 1

    width = 0
    for i in range(n):
        if i == 0:      ## Middle char
            width += 3
        elif i < n-1:   ## Inter-rim chars
            width += 4
        elif i == n-1:  ## Bookend chars
            width += 2
    return width


##########
# Ascii
##########

def get_max_ascii(n) -> int:
    """Returns maximum ascii character to use."""
    return (RANGOLI_START + n) 


# def get_ascii_num()

##########
# Row
##########

def get_num_rowchars(n: int, row: int) -> int:
    """Returns number of distinct chars used in row."""
    row_chars = row
    center_row = (n-1)

    if row > center_row:     # Past center
        row_chars = center_row - (row - center_row)
    return row_chars + 1


def print_row(width: int, num_chars: int, max_char: int):
    """Prints row in the alphabet rangoli."""
    mid = width // 2

    row_chars = [RANGOLI_SPACING for _ in range(width)]
    for i in range(num_chars):
        char_ascii = max_char - (num_chars - i)
        spacing = 2 * i
        char_indices = (mid + spacing, mid - spacing)

        for j in char_indices:
            row_chars[j] = chr(char_ascii)

    row = ''.join(row_chars)
    print(row)
    return


##########
# Rangoli
##########

def print_rangoli(n: int):
    """Prints alphabet rangoli with n chars.

    Args:
        n (int): chars in rangoli

    >>> print_rangoli(n=3):
    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----
    """
    height, width = get_height(n), get_width(n)
    max_char = get_max_ascii(n)

    for i in range(height):
        num_chars = get_num_rowchars(n, row = i)
        print_row(width, num_chars, max_char)
    return


##########
# Tests
##########
def run_tests():
    inputs = [
        1,
        3, 
        5, 
        10
    ]
    for i in inputs:
        print_rangoli(i)
        print()


##########
# Main
##########

if __name__ == '__main__':
    # n = int(input())
    # print_rangoli(n)
    run_tests()