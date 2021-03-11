from sys import stdin
from collections import deque

input = stdin.readline


def tomato_2d(m, n, t):
    day = -2
    dq = deque()
    check = [[False for _ in range(m)] for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 익은 토마토 위치 찾기
    for x in range(n):
        for y in range(m):
            if t[x][y] == 1:
                dq.append((x, y))
                check[x][y] = True
    # 익히는 과정
    while dq:
        loc_x, loc_y = dq.popleft()
        # 4방향 확인
        for di in range(4):
            dxi = dx[di] + loc_x
            dyi = dy[di] + loc_y
            if 0 <= dxi < n and 0 <= dyi < m and not check[dxi][dyi] and t[dxi][dyi] == 0:
                t[dxi][dyi] = t[loc_x][loc_y] + 1
                check[dxi][dyi] = True
                dq.append((dxi, dyi))
    # 최댓값 확인
    for row in t:
        for col in row:
            if col == 0:
                return -1
            day = max(day, col)
    return day-1 if day != 1 and day != -1 else 0


if __name__ == "__main__":
    M, N = map(int, input().split())
    tomato = [list(map(int, input().split())) for _ in range(N)]
    res = tomato_2d(M, N, tomato)
    print(res)
