from sys import stdin

input = stdin.readline


def pocketmon_master(p, i):
    return p[i]


if __name__=="__main__":
    N, M = map(int, input().split())
    pedia = {}
    for i in range(1, N+1):
        ip = input().strip()
        pedia[str(i)] = ip
        pedia[ip] = i
    for _ in range(M):
        print(pocketmon_master(pedia, input().strip()))