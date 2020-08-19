'''
본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다.
입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다.
다음 T줄에는 각각 두 정수 A와 B가 주어진다.
A와 B는 1 이상, 1,000 이하이다.
'''

import sys
T = int(sys.stdin.readline())
for i in range(0,T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
