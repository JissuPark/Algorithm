from sys import stdin

input = stdin.readline


def factorial_0_number(n):
    DP = [1]
    for i in range(1, n + 1):
        DP.append(DP[-1] * i)
    cnt = 0
    for j in str(DP[n])[::-1]:
        if j != '0':
            break
        cnt += 1

    return cnt


if __name__ == "__main__":
    N = int(input())
    res = factorial_0_number(N)
    print(res)
