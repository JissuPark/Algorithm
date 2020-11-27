import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dp = [[0,0] for _ in range(N+1)]
    dp[1] = [0,1]
    for n in range(2, N+1):
        dp[n] = [dp[n-1][1]+dp[n-1][0], dp[n-1][0]]
    print(sum(dp[N]))