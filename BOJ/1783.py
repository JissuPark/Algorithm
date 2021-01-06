import sys
from math import ceil

input = sys.stdin.readline


def sickKnight(n, m):
    if n == 1:
        return 1
    elif n == 2:
        if m > 7:
            return 4
        else:
            return ceil(m / 2)
    else:
        if m >= 7:
            return m - 2
        elif m > 4:
            return 4
        else:
            return m


if __name__ == "__main__":
    N, M = map(int, input().split())
    res = sickKnight(N, M)
    print(res)
