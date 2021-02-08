from sys import stdin, maxsize

input = stdin.readline


def making_1(n):
    DP = [maxsize for _ in range(n)]
    DP.append(0)
    for i in range(n, -1, -1):
        if i*3 <= n: DP[i] = min(DP[i], DP[i*3]+1)
        if i*2 <= n: DP[i] = min(DP[i], DP[i*2]+1)
        if i+1 <= n: DP[i] = min(DP[i], DP[i+1]+1)
    return DP[1]


if __name__ == "__main__":
    N = int(input())
    res = making_1(N)
    print(res)