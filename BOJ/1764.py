from sys import stdin

input = stdin.readline


def off_brand(d, b):
    return sorted(list(d & b))


if __name__ == "__main__":
    N, M = map(int, input().split())
    D = {input().strip() for _ in range(N)}
    B = {input().strip() for _ in range(M)}
    res = off_brand(D, B)
    print(len(res), '\n'.join(res), sep='\n')
