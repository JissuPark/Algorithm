'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

solve)
파이썬에서 리스트에 리스트를 넣으면 포인터처럼 작용 = 하나 삭제하면 같이 삭제됨
'''

import sys, math
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
prime = num.copy()
for n in num:
    if n == 1:
        prime.remove(n)
    for x in range(2, round(math.sqrt(n))+1):
        if n % x == 0:
            prime.remove(n)
            break
print(len(prime))