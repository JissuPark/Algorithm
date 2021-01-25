from sys import stdin
from collections import deque

input = stdin.readline


def card_2(n):
    q = deque([i for i in range(1, n + 1)])
    while len(q) > 1:
        q.popleft()
        card = q.popleft()
        q.append(card)
    return q[0]


if __name__ == "__main__":
    N = int(input())
    res = card_2(N)
    print(res)
