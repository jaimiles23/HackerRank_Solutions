# Solution to [Introduction to Sets](https://www.hackerrank.com/challenges/py-introduction-to-sets)

def average(array):
    """Returns the average of distinct heights."""
    unique_vals = set(array)
    return sum(unique_vals) / len(unique_vals)

    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)