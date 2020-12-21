# Solution to [Text Wrap](https://www.hackerrank.com/challenges/text-wrap)

import textwrap

def wrap(string, max_width):
    newline_char = "\n"
    letters = [char for char in string]
    new_lines = 0
    
    for i in range(len(string)):
        if not i % max_width and i != 0:
            letters.insert(i + new_lines, newline_char)
            new_lines += 1
    return ''.join(letters)

    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)