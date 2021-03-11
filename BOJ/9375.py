from sys import stdin
from functools import reduce

input = stdin.readline


def fashion_king(c):
    if not c:
        return 0
    total = reduce(lambda x, y: x * y, c.values())
    return total - 1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        clothes = dict()
        for _ in range(N):
            cloth, kind = input().split()
            if kind in clothes:
                clothes[kind] += 1
            else:
                clothes[kind] = 2
        res = fashion_king(clothes)
        print(res)
