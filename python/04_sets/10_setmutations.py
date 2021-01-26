# Solution to [Set Mutations](https://www.hackerrank.com/challenges/py-set-mutations)

##########
# Input
##########

def get_init_set() -> set:
    """Returns input set."""
    _ = input()
    return set( map(int, input().split()))


def get_aux_set() -> set:
    """Returns auxiliary set."""
    return set( map(int, input().split()))


def main():
    initial_set = get_init_set()

    num_sets = int(input())
    for i in range( num_sets):
        func, _ = input().split()
        aux_set = get_aux_set()

        code = f"initial_set.{func}(aux_set)"
        exec(code)
    
    print(sum(initial_set))


if __name__ == "__main__":
    main()