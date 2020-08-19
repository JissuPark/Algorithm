'''
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
'''

import sys
N = int(sys.stdin.readline())
for i in range(N):
    print("* " * (int(N/2)+(N%2)))
    if N > 1:
        print(" *" * int(N/2))