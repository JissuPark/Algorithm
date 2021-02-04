from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
input = stdin.readline


def kb_dfs(r, st, it, cnt):
    for et, v in r[it].items():
        if st!=et and v < 101 and v+cnt < r[st][et]:
            r[st][et] = v+cnt
            r[et][st] = v+cnt
            kb_dfs(r, st, et, v+cnt)


def kevin_bacon(r):
    for a in r.keys():
        for b, v in r[a].items():
            if a!=b and v < 101:
                kb_dfs(r, a, b, r[a][b])

    ret = list(map(lambda x: sum(x.values())-101, r.values()))
    return ret.index(min(ret))+1



if __name__ == "__main__":
    N, M = map(int, input().split())
    relations = {j: {i: 101 for i in range(1, N + 1)} for j in range(1, N + 1)}
    for _ in range(M):
        A, B = map(int, input().split())
        relations[A][B] = 1
        relations[B][A] = 1
    res = kevin_bacon(relations)
    print(res)
