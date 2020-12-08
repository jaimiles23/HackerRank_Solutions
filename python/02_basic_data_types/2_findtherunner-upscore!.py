# Solution to [Find the Runner-Up Score!](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_score = max(arr)
    for i in range(len(arr)):
        if arr[i] == max_score:
            arr[i] = - float('inf')
    
    print(max(arr))
