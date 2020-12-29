# Solution to [String Formatting](https://www.hackerrank.com/challenges/python-string-formatting)

def convert_int_to_form(num: int, form_num: int) -> int:
    """Converts decimal integer to specified form number. 

    Supports conversion to octal and binary forms.
    """
    output = 0
    bin_digits = []

    while num > 0:
        num, r = divmod(num , form_num)
        bin_digits.insert(0, r)

    num_digits = len(bin_digits) - 1
    for i in range(num_digits + 1):
        digit = bin_digits[i] * 10 ** (num_digits - i)
        output += digit
    return str(output)


def get_hexa(num: int) -> str:
    """Returns hexadecimal format of decimal integer.
    """
    return str(hex(num))[2:].upper()


def print_formatted(n: int):
    """Prints inclusive range from 1 to n in decimal, octal, hexa, and binary forms."""
    adjustment = len(convert_int_to_form(n, 2))

    for num in range(1, n+1):
        num_forms = [
            str(num), 
            convert_int_to_form(num, 8), 
            get_hexa(num),
            convert_int_to_form(num, 2)
        ]
        for i in range(len(num_forms)):
            end_char = ' ' if i != len(num_forms) - 1 else '\n'
            print(num_forms[i].rjust(adjustment), end = end_char)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)