# Solution to [sWAP cASE](https://www.hackerrank.com/challenges/swap-case)

def swap_case(s):
    def swap_letter(l) -> str:
        if l.islower():
            return l.upper()
        elif l.isupper():
            return l.lower()
        return l
    
    
    return ''.join([swap_letter(char) for char in s])


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)