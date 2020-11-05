# input
from sys import stdin

N, M = map(int, stdin.readline().split())
sumray = list(map(int, stdin.readline().split()))
for i in range(N):
    if i == 0: continue
    sumray[i] += sumray[i - 1]


# solution
def Sumofarray(n, m):
    if n == 1:
        return sumray[m - 1]
    else:
        return sumray[m - 1] - sumray[n - 2]


# output
for _ in range(M):
    fst, snd = map(int, stdin.readline().split())
    print(Sumofarray(fst, snd))
