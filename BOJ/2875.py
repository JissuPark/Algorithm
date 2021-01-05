import sys

input = sys.stdin.readline


def CorI(women, men, intern):
    team = 0
    while women + men - intern >= 3 and men > 0 and women > 1:
        women -= 2
        men -= 1
        team += 1
    return team


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    res = CorI(N, M, K)
    print(res)
