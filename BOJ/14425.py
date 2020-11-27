# 트리는 시간초과
class Node(object):
    def __init__(self, apb):
        self.apb = apb
        self.children = {}
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        for ch in string:
            if ch not in cur.children:
                cur.children[ch]= Node(ch)
            cur = cur.children[ch]
        cur.children['*']='end'

    def search(self, string):
        cur = self.head
        for ch in string:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        if '*' in cur.children:
            return True
# 핵심은 딕셔너리에 in으로 찾을 때 O(1)안에 찾을 수 있다는 것
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
tree = {input().rstrip() for _ in range(N)}
cnt = 0
for _ in range(M):
    string = input().rstrip()
    if string in tree:
        cnt += 1
print(cnt)