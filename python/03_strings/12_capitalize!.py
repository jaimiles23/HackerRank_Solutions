# Solution to [Capitalize!](https://www.hackerrank.com/challenges/capitalize/problem)


# Complete the solve function below.
def solve(s):
    str_list = [c for c in s]

    for i in range(len(str_list)):
        capitalize = False
        if (
            i == 0 or 
            str_list[i - 1] == ' '
        ):
            capitalize = True
            
        if capitalize:
            str_list[i] = str_list[i].capitalize()
    return ''.join(str_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
