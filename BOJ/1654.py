from sys import stdin

input = stdin.readline


def count_cable(c, m):
    return sum(map(lambda x: x // m, c))


def cut_cable(c, n):
    c.sort()
    low = 1
    high = c[-1]
    if count_cable(c,high) >= n:
        return high
    # O(logN) - 이분 탐색
    while True:
        cur = (high + low) // 2
        # O(N) - n개 이상 나오는지 체크
        if count_cable(c, cur) >= n:
            low = cur
            # high는 안되는 경우, low는 되는 경우
            # 두 차이가 1이하이면 더이상 진행 x
            if high - low <= 1:
                break
        else:
            high = cur
    return cur


if __name__ == '__main__':
    K, N = map(int, input().split())
    cables = [int(input()) for _ in range(K)]
    res = cut_cable(cables, N)
    print(res)
