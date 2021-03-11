from sys import stdin
from queue import PriorityQueue

input = stdin.readline


class DPQ:
    def __init__(self):
        self.que = []

    def insert(self, n):
        i = 0
        j = len(self.que) - 1

        while self.que:  # 큐가 비었을때 패스
            if j - i == 1 or self.que[j] == n:
                self.que.insert(j, n)
                break
            if self.que[i] > n:
                i, j = 0, i
            elif self.que[j] < n:
                i, j = j, len(self.que) - 1
            else:



if __name__ == "__main__":
    T = int(input())
    for _ in range(T):

        K = int(input())
        for _ in range(K):
            I, N = input().strip().split()
            if I == 'I':
                pq.insert(int(N))
            elif I == 'D':
                if len(pq.que) == 0:
                    continue
                pq.delete(int(N))
        if len(pq.que) == 1:
            print("EMPTY")
        else:
            print(pq.que[-1], pq.que[1])
