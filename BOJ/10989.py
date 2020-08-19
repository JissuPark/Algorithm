'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

solve)
이 문제는 나오는 수가 적고 양은 많으기떄문에 'Counting Sort'가 해법이다.
'''

import sys
count_arr = [0]*10000
N = int(sys.stdin.readline())
for n in range(N):
    count_arr[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    if count_arr[i] != 0:
        for j in range(count_arr[i]):
            print(i+1)

