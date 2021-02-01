import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline


def cabbage_dfs(cx, cy, g):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        _x, _y = cx + dx[i], cy + dy[i]
        if _x < 0 or _x > len(g)-1 or _y < 0 or _y > len(g[0])-1:
            continue
        if g[_x][_y] == 1:
            g[_x][_y] = 0
            cabbage_dfs(_x, _y, g)


def origanic_cabbage(n, m, g):
    ret = 0
    for x in range(n):
        for y in range(m):
            if g[x][y] == 1:
                g[x][y] = 0
                cabbage_dfs(x, y, g)
                ret += 1
    return ret


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        ground = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().split())
            ground[y][x] = 1
        res = origanic_cabbage(N, M, ground)
        print(res)
