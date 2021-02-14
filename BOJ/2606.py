from sys import stdin
from collections import deque

input = stdin.readline


def virus(n, N):
    visited = [False for _ in range(N + 1)]
    que = deque([1])
    cnt = -1
    # bfs
    while que:
        cur = que.popleft()
        # 다음으로 갈 곳이 없거나 방문한 노드면 넘어감
        if cur not in network or visited[cur]:
            continue
        # 방문 표시
        visited[cur] = True
        # 다음 방문 노드 추가
        for _next in n[cur]:
            # 이미 방문했거나 이미 큐에 있으면 넘어감
            if visited[_next] or _next in que:
                continue
            que.append(_next)
        cnt += 1
    return cnt


if __name__ == "__main__":
    N = int(input())
    T = int(input())
    network = dict()
    for _ in range(T):
        n1, n2 = map(int, input().split())
        if n1 not in network:
            network[n1] = [n2]
        else:
            network[n1].append(n2)
        if n2 not in network:
            network[n2] = [n1]
        else:
            network[n2].append(n1)
    res = virus(network, N)
    print(res)
