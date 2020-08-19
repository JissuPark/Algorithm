'''
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

ex)
입력
3
출력
*
**
***
**
*
'''

import sys

N = int(sys.stdin.readline())
for i in range(1, 2*N):
    if i < N:
        print("*"*i)
    else:
        print("*"*(2*N-i))