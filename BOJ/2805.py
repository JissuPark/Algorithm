from sys import stdin
from collections import Counter
input = stdin.readline

# Counter 풀이
def cut_tree(t, m):
    low, high = 0, max(t)
    while True:
        cur = (low + high) // 2
        if sum(map(lambda x: (x[0] - cur)*x[1] if x[0] - cur > 0 else 0, t.items())) >= m:
            low = cur
            if high - low <= 1:
                break
        else:
            high = cur
    return cur


if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = Counter(list(map(int, input().split())))
    res = cut_tree(trees, M)
    print(res)

# 배열 풀이
'''
def cut_tree(t, m):
    t.sort()
    low, high = 0, t[-1]
    while True:
        cur = (low + high)//2
        if sum(map(lambda x: x-cur if x-cur > 0 else 0, t)) >= m:
            low = cur
            if high - low <= 1:
                break
        else:
            high = cur
    return cur


if __name__=="__main__":
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    res = cut_tree(trees, M)
    print(res)
'''
