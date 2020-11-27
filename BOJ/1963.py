import sys
from collections import deque
input = sys.stdin.readline

def erasto():
    for p in range(2,100):
        if Prime[p]:
            for q in range(p*p, 10000, p):
                Prime[q] = False
def bfs():
    while q:
        cur = q.popleft()
        if cur == prime2:
            return visit[prime2]
        for i in range(4):
            plist = list(str(cur))
            for j in range(10):
                plist.pop(i)
                plist.insert(i,j)
                pstr = int(''.join(map(str,plist)))
                if len(str(pstr))==4 and Prime[pstr] and visit[pstr] > visit[cur]+1:
                    q.append(pstr)
                    visit[pstr] = visit[cur]+1
    return 'Impossible'

if __name__ == "__main__":
    T = int(input())
    maxsize = 10000
    Prime = [True] * maxsize
    erasto()
    for _ in range(T):
        prime1, prime2 = map(int, input().split())
        visit = [maxsize]*maxsize
        visit[prime1] = 0
        q = deque([prime1])
        print(bfs())