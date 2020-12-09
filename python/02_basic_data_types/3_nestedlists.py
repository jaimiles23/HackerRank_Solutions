# Solution to [Nested Lists](https://www.hackerrank.com/challenges/nested-list)

"""
I implement a naive solution. A better time complexity solution may:
    1. Dynamically create the list a binary search
    2. Returns elements with the second lowest value
or, alternatively, create a dictionary of score keys that track names of users with the second lowest score.
"""


if __name__ == '__main__':
    ## Create names
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append((name, score))
    
    ## Sort list
    names.sort(key = lambda x: (x[1], x[0]))

    ## Tracking vars
    min_value = names[0][1]
    flag_second_val = False
    second_min_val = None


    for n in names:
        val = n[1]
        if val == min_value:
            continue

        elif second_min_val is None:
            second_min_val = val

        if val == second_min_val:
            print(n[0])
        
            

    
