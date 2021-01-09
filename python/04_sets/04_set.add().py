# Solution to [Set .add()](https://www.hackerrank.com/challenges/py-set-add)

def main():
    country_stamps = set()
    n = int(input())

    for _ in range(n):
        country_stamps.add(input())
    
    print(len(country_stamps))


if __name__ == "__main__":
    main()