'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
첫 째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
'''

import sys

# list의 함수를 이용해 푸는 방법
int_list = list()
for i in range(9):
    int_list.append(int(sys.stdin.readline()))
print(max(int_list))
print(int_list.index(max(int_list))+1)

#비교를 통해서 값과 인덱스를 구하는 방법
max_int = 0
max_idx = 0
for i in range(1,10):
    intput = int(sys.stdin.readline())
    if max_int < intput:
        max_int = intput
        max_idx = i
print(max_int)
print(max_idx)