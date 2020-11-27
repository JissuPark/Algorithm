import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


def prim(start):
    mst = 0
    connected = set()
    connected.add(start)
    edgelist = graph[start]
    heapq.heapify(edgelist)
    while edgelist:
        weight, node1, node2 = heapq.heappop(edgelist)
        if node2 not in connected:
            connected.add(node2)
            mst += weight
            for edge in graph[node2]:
                if edge[2] not in connected:
                    heapq.heappush(edgelist, edge)
    return mst


if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        A, B, C = map(int, input().split())
        graph[A].append((C, A, B))
        graph[B].append((C, B, A))
    print(prim(1))