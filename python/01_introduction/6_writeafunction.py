# Solution to [Write a function](https://www.hackerrank.com/challenges/write-a-function)

def is_leap(year: int) -> bool:
    """Returns boolean if year is a leap year.

    Args:
        year (int): year

    Returns:
        bool: is leap year
    """

    if year % 4:    # every 4 years
        return False

    if not year % 100 and year % 400:
        return False
    return True

year = int(input())
print(is_leap(year))