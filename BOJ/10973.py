import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    P = list(map(int, input().split()))
    if P == sorted(P):
        print(-1)
    else:
        idx = 0
        # find index to split
        for i in range(N-1, 0, -1):
            if P[i-1]>P[i]:
                idx = i
                break
        # find index of right max num
        maxidx = i
        for j in range(i, N):
            if P[i-1]>P[j] and P[maxidx]<P[j]:
                maxidx = j
        # swap
        P[i-1] , P[maxidx] = P[maxidx] , P[i-1]
        # sort right side
        P = P[:i]+sorted(P[i:], reverse=True)
        # sublist sort is not working
        # P[i-1:].sort(reverse=True)

        # print
        print(' '.join(map(str, P)))
