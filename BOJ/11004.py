import sys
#input
N, K = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split(' ')))
#solution
def Kthnum(numlist, k):
    return sorted(numlist)[k-1]
#output
print(Kthnum(alist, K))