from sys import stdin, maxsize
from collections import deque

input = stdin.readline


def exploring_labyrinth(l, n, m):
    cost = [[maxsize for _ in range(m)] for _ in range(n)]
    cost[0][0] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dq = deque([[0, 0]])
    while dq:
        cur = dq.popleft()
        l[cur[0]][cur[1]] = '0'
        # 4방향 찾기
        for di in range(4):
            # 갈 수 있는 곳이 있으면 큐에 저장
            dxi = cur[0] + dx[di]
            dyi = cur[1] + dy[di]
            if 0 <= dxi < n and 0 <= dyi < m:
                if l[dxi][dyi] == '1' and [dxi, dyi] not in dq:
                    dq.append([dxi, dyi])
                # 최솟값 + 1
                cost[cur[0]][cur[1]] = min(cost[cur[0]][cur[1]], cost[dxi][dyi] + 1)
    return cost[-1][-1]


if __name__ == "__main__":
    N, M = map(int, input().split())
    labyrinth = [list(input().strip()) for _ in range(N)]
    res = exploring_labyrinth(labyrinth, N, M)
    print(res)
