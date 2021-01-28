from sys import stdin

input = stdin.readline


def josephus(n, k):
    circle = [i for i in range(1, n + 1)]
    idx = 0
    ret = []
    while circle:
        idx += k - 1
        if idx >= len(circle):
            idx = idx % len(circle)
        ret.append(str(circle.pop(idx)))
    return ret


if __name__ == "__main__":
    N, K = map(int, input().split())
    res = josephus(N, K)
    print(f"<{', '.join(res)}>")
