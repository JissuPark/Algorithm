from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10000)


def z(n, x, y, cnt):
    if n == 1:
        if x == r and y == c:
            return cnt
        elif x == r and y + 1 == c:
            return cnt + 1
        elif x + 1 == r and y == c:
            return cnt + 2
        else:
            return cnt + 3
    else:
        if x + 2 ** (n - 1) > r:
            if y + 2 ** (n - 1) > c:
                return z(n - 1, x, y, cnt)
            else:
                return z(n - 1, x, y + 2 ** (n - 1), cnt + 2 ** (2 * n - 2))
        else:
            if y + 2 ** (n - 1) > c:
                return z(n - 1, x + 2 ** (n - 1), y, cnt + 2 * 2 ** (2 * n - 2))
            else:
                return z(n - 1, x + 2 ** (n - 1), y + 2 ** (n - 1), cnt + 3 * 2 ** (2 * n - 2))


if __name__ == "__main__":
    N, r, c = map(int, input().split())
    res = z(N, 0, 0, 0)
    print(res)

# time over
'''
def Z(a, n, x, y, c):
    if n == 1:
        a[x][y], a[x][y+1], a[x+1][y], a[x+1][y+1] = c, c+1, c+2, c+3
    else:
        Z(a, n-1, x, y, c)
        Z(a, n-1, x, y+2**(n-1), c+2**(2*n-2))
        Z(a, n-1, x+2**(n-1), y, c+2*2**(2*n-2))
        Z(a, n-1, x+2**(n-1), y+2**(n-1), c+3*2**(2*n-2))


if __name__ == "__main__":
    N, r, c = map(int, input().split())
    array = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
    Z(array, N, 0, 0, 0)
    print(array[r][c])
'''
