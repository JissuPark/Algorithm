'''
두 정수 A와 B(0 < A, B < 10)를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다.
'''

import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {A+B}')