# Solution to [Merge the Tools!](https://www.hackerrank.com/challenges/merge-the-tools)

def merge_the_tools(string: str, k: int):
    lower_index = 0
    for i in range(k, len(string) + 1, k):
        substr = string[lower_index : i]
        lower_index += k

        used_chars = set()
        substr = [char for char in substr]
        del_chars = 0

        for i in range(len(substr)):
            if substr[i - del_chars] not in used_chars:
                used_chars.add(substr[i - del_chars])
                continue
            
            ## Remove from substr
            del substr[i - del_chars]
            del_chars += 1
        
        print(''.join(substr))


def test():
    """Runs tests for merge the tools!"""
    tests = (
        ("AABCAAADA", 3),
    )

    for t in tests:
        merge_the_tools(t[0], t[1])



if __name__ == '__main__':
    # string, k = input(), int(input())
    # merge_the_tools(string, k)

    test()