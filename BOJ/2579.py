from sys import stdin

input = stdin.readline


def stair_climbing(s, n):
    if len(s) < 3:
        return sum(s)
    DP = [[s[0], s[0]], [s[0] + s[1], s[1]]]
    for i in range(2, n):
        DP.append([DP[i - 1][1] + s[i], max(DP[i - 2][0], DP[i - 2][1]) + s[i]])
    print(DP)
    return max(DP[n - 1])


if __name__ == "__main__":
    N = int(input())
    stair = [int(input()) for _ in range(N)]
    res = stair_climbing(stair, N)
    print(res)
