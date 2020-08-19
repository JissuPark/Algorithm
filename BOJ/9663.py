'''
문제)
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력)
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''

import sys
N = int(sys.stdin.readline())
check = [[False]*N for n in range(N)]
cnt = 0

def disable(X,Y):
    arr = list()
    for n in range(N):
        if check[n][Y] == False:
            check[n][Y] = True
            arr.append([n,Y])
        if check[X][n] == False:
            check[X][n] = True
            arr.append([X,n])
        if X-n >= 0 and n != 0:
            if Y-n >= 0 and check[X-n][Y-n]==False:
                check[X-n][Y-n] = True
                arr.append([X-n,Y-n])
            if Y+n < N and check[X-n][Y+n]==False:
                check[X-n][Y+n] = True
                arr.append([X-n, Y+n])
        if X+n < N and n != 0:
            if Y-n >= 0 and check[X+n][Y-n]==False:
                check[X+n][Y-n] = True
                arr.append([X+n,Y-n])
            if Y+n < N and check[X+n][Y+n]==False:
                check[X+n][Y+n] = True
                arr.append([X+n,Y+n])
    return arr


def enable(arr):
    for ar in arr:
        check[ar[0]][ar[1]]=False

def queen(num, cnt):
    if num == 0:
        for i in range(N):
            if check[num][i] == False:
                cnt += 1
        return cnt
    for m in range(N):
        if check[num][m] == False:
            check[num][m] = True
            arrcheck = disable(num,m)
            cnt = queen(num-1,cnt)
            enable(arrcheck)
            check[num][m] = False
    return cnt


print(queen(N-1,cnt))