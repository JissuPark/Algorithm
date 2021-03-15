from sys import stdin

input = stdin.readline


def find_way(g):
    for i in range(len(g)):
        check = [False for _ in range(len(g))]

        def dfs(s, n):
            for j in range(len(g)):
                if g[n][j] and not check[j]:
                    g[s][j] = 1
                    check[j] = True
                    dfs(s, j)

        dfs(i, i)
    return g


if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    res = find_way(graph)
    for row in res:
        for col in row:
            print(col, end=' ')
        print()
