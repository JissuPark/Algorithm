from sys import stdin

input = stdin.readline


def paper_check(p, n, x, y):
    prev = {p[x][y]}
    for i in range(n):
        cur = set(p[x + i][y:y + n])
        if len(cur) != 1 or cur != prev:
            return False
    return True


def paper_count(p, n, x, y):
    ret = []
    if n == 1:
        return [p[x][y]]
    if paper_check(p, n, x, y):
        return [p[x][y]]
    for xi in range(3):
        for yi in range(3):
            ret.extend(paper_count(p, n // 3, x + xi * (n // 3), y + yi * (n // 3)))
    return ret


if __name__ == "__main__":
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    res = paper_count(paper, N, 0, 0)
    print(res.count(-1), res.count(0), res.count(1), end='\n')
