from sys import stdin
from collections import Counter
input = stdin.readline


def number_card_2(sg, c):
    ret = []
    for n in c:
        if n in sg.keys():
            ret.append(str(sg.get(n)))
        else:
            ret.append('0')
    return ret


if __name__ == "__main__":
    N = int(input())
    SG = list(map(int, input().split()))
    M = int(input())
    cards = list(map(int, input().split()))
    res = number_card_2(Counter(SG), cards)
    print(' '.join(res))