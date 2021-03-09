# Solution to [Check Subset](https://www.hackerrank.com/challenges/py-check-subset)

def get_set() -> set:
    """returns set"""
    _ = input()
    return set(map(int, input().split()))


def main():
    for _ in range(int(input())):
        set_a = get_set()
        set_b = get_set()
        a_not_b = set_a.difference(set_b)
        print(False if a_not_b else True)




if __name__ == "__main__":
    main()