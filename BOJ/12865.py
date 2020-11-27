import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    values = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for row in range(1, N+1):
        W, V = map(int, input().split())
        for col in range(1, K+1):
            if W > col:
                values[row][col] = values[row-1][col]
            else:
                values[row][col] = max(values[row-1][col], values[row-1][col-W] + V)
    #print(*values, sep='\n')
    print(values[N][K])
