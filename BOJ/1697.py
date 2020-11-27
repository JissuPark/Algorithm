import sys
from collections import deque
input = sys.stdin.readline


# solution
def bfs():
    while q:
        cur = q.popleft()
        if cur == K:
            return visited[cur]
        pushnext(cur+1, cur)
        pushnext(cur-1, cur)
        pushnext(cur*2, cur)


def pushnext(nxt, cur):
    if maxsize > nxt >= 0 and visited[cur]+1 < visited[nxt]:
        visited[nxt] = visited[cur]+1
        q.append(nxt)


# main
if __name__ == "__main__":
    N, K = map(int, input().split())
    maxsize = 100001
    visited = [maxsize]*maxsize
    visited[N] = 0
    q = deque([N])
    print(bfs())