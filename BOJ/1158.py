import sys
#input
N, K = map(int, sys.stdin.readline().split())
#solution
def yosefuse(n, k):
    answer = []
    circle = [i for i in range(1,n+1)]
    rmv = 0
    while circle:
        rmv = (rmv+k-1)%len(circle)
        answer.append(circle.pop(rmv))
    return answer
#output
print(str(yosefuse(N,K)).replace('[','<').replace(']','>'))