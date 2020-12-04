import sys
# from itertools import permutations
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    P = list(map(int, input().split()))
    if P == sorted(P,reverse=True):
        print(-1)
    else:
        idx = 0
        for i in range(N-1, 0, -1):
            if P[i-1]<P[i]:
                idx = i
                break
        left = P[:i]
        right = P[i-1:]
        target = min([x for x in right if x > left[-1]])
        left.pop(-1)
        left.append(target)
        right.remove(target)
        right.sort()
        print(' '.join(map(str,left+right)))

    ''' 메모리 초과
    check = False
    print(sorted(permutations(list(range(1,N+1)))))
    for perm in sorted(permutations(list(range(1,N+1)))):
        if check:
            print(' '.join(map(str, perm)))
            break
        if P == ' '.join(map(str,perm)):
            check = True
    else:
        print(-1)
    '''