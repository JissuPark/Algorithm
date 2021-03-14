from sys import stdin
import heapq

input = stdin.readline


def max_heap(x):
    h = []
    ret = []
    for num in x:
        if num == 0:
            ret.append(0 if not h else heapq.heappop(h)[1])
        else:
            heapq.heappush(h, (-num, num))
    return ret


if __name__ == "__main__":
    N = int(input())
    X = []
    for _ in range(N):
        X.append(int(input()))
    res = max_heap(X)
    print('\n'.join(map(str, res)))
