import sys
sys.setrecursionlimit(10000)
# input
input = sys.stdin.readline
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
mincost = sys.maxsize
visited = [False] * N
#solution
def dfs(str, cur, total):
    global mincost, N
    if cost[cur][str] != 0 and False not in visited:
        total += cost[cur][str]
        mincost = min(total, mincost)
        #print(f'{str} cost = {mincost}')
        return
    for i in range(N):
        if cost[cur][i] == 0 or visited[i]:
            continue
        visited[i] = True
        dfs(str, i, total+cost[cur][i])
        visited[i] = False
# 항상 순회할 수 있기 때문에 어느 점 하나를 골라서 돌려도 된다.
# str을 지운 함수를 만들면 pypy3안써도 통과한다.
# 현재 코드는 아래 for문 덕에 pypy3로만 통과가능하다.
for n in range(N):
    visited[n] = True
    dfs(n, n, 0)
    visited[n] = False
#output
print(mincost)