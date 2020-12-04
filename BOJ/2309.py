import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == '__main__':
    littles = []
    for _ in range(9):
        littles.append(int(input()))
    for combi in combinations(littles, 7):
        if sum(list(combi)) == 100:
            combi = sorted(list(combi))
            print('\n'.join((map(str, combi))))
            break
