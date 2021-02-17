from sys import stdin

input = stdin.readline


def ioioi(n, m, s):
    pn = 0
    cnt = 0
    i = 1
    while i < m - 1:
        if s[i - 1] == 'I' and s[i] == 'O' and s[i + 1] == 'I':
            pn += 1
            if pn == n:
                cnt += 1
                pn -= 1
            i += 2
        else:
            pn = 0
            i += 1
    return cnt


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    S = input().strip()
    res = ioioi(N, M, S)
    print(res)
