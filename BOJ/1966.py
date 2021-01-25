from sys import stdin
from collections import deque

input = stdin.readline


def find_priority(q):
    for p in q:
        if q[0] < p:
            return False
    return True


def print_queue(q, m):
    idx = 1
    while q:
        if find_priority(q):
            if m == 0:
                break
            else:
                m -= 1
            q.popleft()
            idx += 1
        else:
            if m == 0:
                m += len(q) - 1
            else:
                m -= 1
            paper = q.popleft()
            q.append(paper)
    return idx


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        queue = deque(map(int, input().split()))
        res = print_queue(queue, M)
        print(res)
