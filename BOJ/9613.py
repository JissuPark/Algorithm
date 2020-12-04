import sys
from math import gcd
from itertools import combinations
input = sys.stdin.readline


def gcdsum(n):
    res = 0
    for a,b in combinations(n,2):
        res += gcd(a,b)
    return res


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        num = list(map(int, input().split()))
        n = num.pop(0)
        print(gcdsum(num))
