from sys import stdin
from collections import deque

input = stdin.readline


def tomato(m, n, h, b):
    day = 0
    que = deque()
    check = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if b[z][x][y] == 1:
                    que.append((z, x, y))
                    check[z][x][y] = True

    dx = [0, 0, 1, -1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while que:
        cur = que.popleft()
        z, x, y = cur
        for di in range(6):
            dxi = dx[di] + x
            dyi = dy[di] + y
            dzi = dz[di] + z

            if 0 <= dxi < n and 0 <= dyi < m and 0 <= dzi < h and not check[dzi][dxi][dyi]:
                if b[dzi][dxi][dyi] == 0:
                    b[dzi][dxi][dyi] = b[z][x][y] + 1
                    que.append((dzi, dxi, dyi))
                    check[dzi][dxi][dyi] = True

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if b[z][x][y] == 0:
                    return -1
                day = max(day, b[z][x][y])

    return 0 if day == 1 or day == -1 else day - 1


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    res = tomato(M, N, H, box)
    print(res)
