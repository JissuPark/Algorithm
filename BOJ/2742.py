'''
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

import sys
N = int(sys.stdin.readline())
for i in range(N, 0, -1):
    print(i)