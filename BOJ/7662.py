from sys import stdin
import heapq

input = stdin.readline


def double_priority_queue(q, ci, cd):
    heap_max = []
    heap_min = []
    cnt = dict()

    if ci <= cd:
        return "EMPTY"
    for op, n in q:
        if op == "I":
            heapq.heappush(heap_max, (-n, n))
            heapq.heappush(heap_min, (n, n))
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1
        elif op == "D" and len(cnt) == 0:
            continue
        elif op == "D" and n == "1":
            _pop = heapq.heappop(heap_max)
            cnt[_pop] -= 1
            if len(cnt[_pop]) == 0:
                del(cnt[_pop])
        elif op == "D" and n == "-1":
            heap.popleft(0)
    return f'{heap[-1]} {heap[0]}' if heap else "EMPTY"


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        K = int(input())
        Q = []
        cnt_i, cnt_d = 0, 0
        for _ in range(K):
            i1, i2 = input().split()
            if i1 == "I":
                cnt_i += 1
            else:
                cnt_d += 1
            if cnt_i == cnt_d:
                continue
            Q.append((i1, int(i2)))
        res = double_priority_queue(Q, cnt_i, cnt_d, cnt)
        print(res)
