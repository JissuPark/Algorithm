from math import gcd
from sys import stdin

input = stdin.readline


def acin(m, n, x, y):
    if m > n:
        m, n, x, y = n, m, y, x

    tmp = y
    while tmp < (m * n // gcd(m, n) + 1):
        t = tmp % m if tmp % m != 0 else m
        if t == x:
            return tmp
        tmp += n
    return -1
'''
4
39999 2 39998 2
8 2 4 2
12 6 12 6
10 1 5 1
'''

'''
def acin(m, n, x, y):
    limit = m * n // gcd(m, n)
    for i in range(1, limit + 1):
        _x = i % m if i % m != 0 else m
        _y = i % n if i % n != 0 else n
        if _x == x and _y == y:
            return i
    return -1

'''

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, X, Y = map(int, input().split())
        res = acin(M, N, X, Y)
        print(res)
