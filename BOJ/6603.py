import sys
from itertools import combinations
# input
input = sys.stdin.readline

# 숫자 리스트 문자열로 변경하는 법 잊지말기
while True:
    k, *klist = list(map(int, input().split()))
    if k == 0:
        break
    combi = combinations(klist, 6)
    for c in combi:
        print(' '.join(map(str,c)))
    print()
