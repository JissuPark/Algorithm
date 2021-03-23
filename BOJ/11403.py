from sys import stdin
input = stdin.readline


def find_way(n, g):
    for stopover in range(n):
        for start in range(n):
            for end in range(n):
                if g[start][stopover] and g[stopover][end]:
                    g[start][end] = 1


if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    find_way(N, graph)
    for line in graph:
        print(' '.join(map(str, line)))