from functools import reduce
from sys import stdin

input = stdin.readline


def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    elif k == n:
        return 1
    n1 = reduce(lambda x, y: x * y, [i for i in range(k + 1, n + 1)])
    n2 = reduce(lambda x, y: x * y, [i for i in range(1, n - k + 1)])
    return n1 // n2


if __name__ == "__main__":
    N, K = map(int, input().split())
    res = binomial_coefficient(N, K)
    print(res)
