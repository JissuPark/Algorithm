from sys import stdin

input = stdin.readline


def count_connections(n, g):
    check = [0 for _ in range(n + 1)]
    idx = 0
    for i in range(1, n + 1):
        if check[i] != 0:
            continue
        idx += 1
        que = set([i])
        check[i] = idx
        while que:
            node = que.pop()
            for next in g[node]:
                if check[next] != 0:
                    continue
                que.add(next)
                check[next] = idx
    return max(check)


if __name__ == '__main__':
    graph = {}
    N, M = map(int, input().split())
    for a in range(1,N+1):
        graph[a] = []
    for _ in range(M):
        u, v = map(int, input().split())
        graph[v].append(u)
        graph[u].append(v)
    res = count_connections(N, graph)
    print(res)
