import sys
# input
N = int(sys.stdin.readline())
Deck = list(map(int, ''.join(sys.stdin).strip().split('\n')))
# solution
def card(card):
    answer = {}
    for c in card:
        if c in answer:
            answer[c] += 1
        else:
            answer[c] = 1
    return sorted(answer.items(), key=lambda e: (-e[1], e[0]))[0][0]
# output
print(card(Deck))
