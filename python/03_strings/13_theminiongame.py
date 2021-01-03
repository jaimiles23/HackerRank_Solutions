# Solution to [The Minion Game](https://www.hackerrank.com/challenges/the-minion-game)
VOWELS = 'AEIOU'

def minion_game(word):
    p1_name, p2_name = 'Kevin', 'Stuart'
    p1_score, p2_score = 0, 0
    
    for i in range(len(word)):
        points = len(word) - i
        if word[i] in VOWELS:
            p1_score += points
        else:
            p2_score += points
    

    if p1_score > p2_score:
        print(p1_name, p1_score)
    elif p2_score > p1_score:
        print(p2_name, p2_score)
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = input()
    minion_game(s)