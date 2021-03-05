from sys import stdin

input = stdin.readline


def coordinate_compression(x):
    d = dict()
    ret = list()
    for i, s in enumerate(sorted(list(set(x)))):
        d[s] = i
    for y in x:
        ret.append(str(d[y]))
    return ret


if __name__ == "__main__":
    N = int(input())
    X = list(map(int, input().split()))
    res = coordinate_compression(X)
    print(' '.join(res))
