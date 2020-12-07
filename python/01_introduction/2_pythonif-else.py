# Solution to [Python If-Else](https://www.hackerrank.com/challenges/py-if-else/problem)

#!/bin/python3

if __name__ == '__main__':
    weird = "Weird"
    not_weird = "Not Weird"
    
    n = int(input().strip())
    odd = (n % 2 == 1)
    even = not odd
    
    if odd:
        print(weird)
    elif even and 2 <= n <= 5:
        print(not_weird)
    elif even and 6 <= n <= 20:
        print(weird)
    elif even and n > 20:
        print(not_weird)