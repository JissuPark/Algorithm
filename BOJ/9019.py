from sys import stdin
from collections import deque

input = stdin.readline


def dslr(a, b):
    que = deque([(a, "")])
    visit = [False for _ in range(10001)]
    visit[a] = True
    # R과 L은 4번까지 돌면 제자리 즉 먼저 확인해야함
    while que:
        c, operation = que.popleft()
        print(c, operation)
        if c == b:
            return operation
        # b가 더 크면 증가 시켜야하므로 D
        d = (c * 2) % 10000
        if not visit[d]:
            que.append((d, operation + "D"))
            visit[d] =True
        # b가 더 작으면 감소 시켜야하므로 S
        d = (c - 1) % 10000
        if not visit[d]:
            que.append((d, operation + "S"))
            visit[d] = True
        d = (c % 1000) * 10 + c // 1000
        if not visit[d]:
            que.append((d, operation + "L"))
            visit[d] = True
        d = (c % 10) * 1000 + c // 10
        if not visit[d]:
            que.append((d, operation + "R"))
            visit[d] = True

    return operation


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        res = dslr(A, B)
        print(res)

'''
def dslr(a, b):
    que = deque([(a, "")])
    visit = [False for _ in range(10001)]
    # R과 L은 4번까지 돌면 제자리 즉 먼저 확인해야함
    while que:
        c, operation = que.popleft()
        visit[int(c)] = True
        if c == b:
            return operation
        # b가 더 크면 증가 시켜야하므로 D
        d = str(int(c) * 2 % 10000).zfill(4)
        if not visit[int(d)]:
            que.append((d, operation + "D"))
        # b가 더 작으면 감소 시켜야하므로 S
        d = str(int(c) - 1).zfill(4) if c > '0001' else '9999'
        if not visit[int(d)]:
            que.append((d, operation + "S"))
        d = c[1:]+c[0]
        if not visit[int(d)]:
            que.append((d, operation+"L"))
        d = c[3]+c[:3]
        if not visit[int(d)]:
            que.append((d, operation+"R"))

    return operation


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = input().split()
        res = dslr(A.zfill(4), B.zfill(4))
        print(res)
'''
