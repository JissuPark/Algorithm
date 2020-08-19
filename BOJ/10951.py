'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

solve) 딱히 조건은 없으나 입력의 종단점이 주어지지 않는 것이 포인트이다.
* 보통 풀이는 for문과 sys.stdin을 사용해 문자열의 종단점까지 받아서 푸는 듯해보인다.
'''

import sys
for input in sys.stdin:
    A, B = map(int, input.split())
    print(A+B)
    # 아래와 같이 한번에 출력하는 것도 가능
    # print(sum(map(int, input.split())))