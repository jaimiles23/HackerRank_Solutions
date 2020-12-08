# Solution to [Print Function](https://www.hackerrank.com/challenges/python-print)

    
if __name__ == '__main__':
    n = int(input())
    print(*(range(1, n+1)), sep = '', end = '')