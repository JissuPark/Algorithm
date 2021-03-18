from sys import stdin
from itertools import combinations

input = stdin.readline


def delivery_chicken(n, m, h, c):
    ret = 1e9
    for combi in combinations(c, m):
        c_dist = 0
        for hi in h:
            c_dist += min(map(lambda ci: abs(hi[0] - ci[0]) + abs(hi[1] - ci[1]), combi))
        ret = min(ret, c_dist)
    return ret


if __name__ == "__main__":
    N, M = map(int, input().split())
    house = []
    chicken = []
    for x in range(N):
        info = list(map(int, input().split()))
        for y in range(N):
            if info[y] == 1:
                house.append((x, y))
            elif info[y] == 2:
                chicken.append((x, y))
    res = delivery_chicken(N, M, house, chicken)
    print(res)
