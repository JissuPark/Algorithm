from sys import stdin

input = stdin.readline


def padovan_sequence(n):
    dp = [0, 1, 1, 1, 2, 2]
    for i in range(6, n + 1):
        dp.append(dp[i - 1] + dp[i - 5])
        # print(f'{dp[i-1]} + {dp[i-5]} = {dp[i]}')
    return dp[n]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        res = padovan_sequence(N)
        print(res)
