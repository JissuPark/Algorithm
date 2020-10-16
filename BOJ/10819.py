import sys
from itertools import permutations


def maxsub(array):
    res = 0
    for i in range(len(array)-1):
        res += abs(array[i]-array[i+1])
    return res


def solution(array):
    maxsum = 0
    for permut in permutations(array, len(array)):
        maxsum = maxsub(permut) if maxsum < maxsub(permut) else maxsum
    return maxsum


#input
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
#output
print(solution(A))