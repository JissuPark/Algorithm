import sys
input = sys.stdin.readline
INF = sys.maxsize


def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a-1][b-1] = min(dist[a-1][b-1], c)
    # cost for itself is 0
    for i in range(n):
        dist[i][i] = 0
    floyd()
    # change 0 if no way to go
    for x in range(n):
        for y in range(n):
            if dist[x][y] == INF:
                dist[x][y] = 0
    # output
    for d in dist:
        print(' '.join(map(str, d)))