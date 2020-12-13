# Solution to [Find a string](https://www.hackerrank.com/challenges/find-a-string)

def count_substring(string, sub_string) -> int:
    """Returns the count of sub_string occurences in string.
    
    Uses a moving window to check sections of the string for the substring.
    """
    count = 0
    str_window = []
    
    for i in range(len(string)):
        str_window.append(string[i])
        if len(str_window) > len(sub_string):
            del str_window[0]
        
        if ''.join(str_window) == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)