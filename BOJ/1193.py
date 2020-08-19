'''
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
'''

import sys
import math
# x = int(sys.stdin.readline())
for x in range(1, 10000000):
    n = round(math.sqrt(x*2))
    idx = x - (n*(n-1)//2) - 1
    if n % 2: # 홀수 - 분모에 더하기 / 분자에 빼기
        print(f'{n - idx}/{1 + idx}')
    else: # 짝수 - 분모에서 빼기 / 분자에 더하기
        print(f'{1 + idx}/{n - idx}')