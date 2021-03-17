from sys import stdin
from collections import deque

input = stdin.readline


def tetromino(a, n, m):
    ret = 0
    di = [
        # 일자
        [[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]],
        # 네모
        [[0, 0], [0, 1], [1, 0], [1, 1]],
        # 기억
        [[0, 0], [0, 1], [0, 2], [1, 0]], [[0, 0], [0, 1], [0, 2], [-1, 2]],
        [[0, 0], [1, 0], [1, 1], [1, 2]], [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [1, 0], [2, 0], [2, -1]],
        [[0, 0], [0, 1], [1, 0], [2, 0]], [[0, 0], [0, 1], [1, 1], [2, 1]],
        # 볼록할 철
        [[0, 0], [0, 1], [0, 2], [1, 1]], [[0, 0], [0, 1], [0, 2], [-1, 1]],
        [[0, 0], [1, 0], [1, 1], [2, 0]], [[0, 0], [1, 0], [2, 0], [1, -1]],
        # 번개
        [[0, 0], [1, 0], [1, -1], [2, -1]], [[0, 0], [1, 0], [1, 1], [2, 1]],
        [[0, 0], [0, 1], [-1, 1], [-1, 2]], [[0, 0], [0, 1], [1, 1], [1, 2]]
    ]
    for x in range(n):
        for y in range(m):
            for d in di:
                four = 0
                for i in range(4):
                    xi = x + d[i][0]
                    yi = y + d[i][1]
                    if 0 <= xi < n and 0 <= yi < m:
                        four += a[xi][yi]
                ret = max(ret, four)
    return ret


'''
def tetromino(a, n, m):
    ret = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for x in range(n):
        for y in range(m):
            dp = [[0 for _ in range(m)] for _ in range(n)]
            dp[x][y] = a[x][y]
            que = deque([(x, y)])
            _max = 0
            while que:
                _x, _y = que.popleft()
                for di in range(4):
                    dxi = _x + dx[di]
                    dyi = _y + dy[di]
                    if 0 <= dxi < n and 0 <= dyi < m and dp[dxi][dyi] == 0 and abs(dxi - x) + abs(dyi - y) < 4:
                        dp[dxi][dyi] = max(dp[dxi][dyi], dp[_x][_y] + a[dxi][dyi])
                        que.append((dxi, dyi))
                        _max = max(_max, dp[dxi][dyi])
            ret = max(ret, _max)

    return ret
'''

if __name__ == "__main__":
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    res = tetromino(array, N, M)
    print(res)
