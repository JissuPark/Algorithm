'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
'''

import sys, math
N = int(sys.stdin.readline())
print(math.factorial(N))