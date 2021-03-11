from sys import stdin, stdout
input = stdin.readline
print = stdout.write

if __name__ == "__main__":
    memo = dict()
    N, M = map(int, input().split())
    for _ in range(N):
        site, passwd = input().split()
        memo[site] = passwd
    for _ in range(M):
        m = input().strip()
        print(memo[m]+'\n')
