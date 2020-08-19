'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

import sys


# 시간 초과 = O(nlogn)
def mergesort(array):
    merge = list()
    if len(array) > 1:
        first = mergesort(array[:len(array)//2])
        second = mergesort(array[len(array)//2:])
        for i in range(len(array)): # second이 하나 더 많을 수도 있으니까 first 길이에 맞추고
            if len(first) == 0:
                merge.append(second.pop(0))
            elif len(second) == 0:
                merge.append(first.pop(0))
            elif first[0] < second[0]:
                merge.append(first.pop(0))
            else:
                merge.append(second.pop(0))
        return merge
    else:
        return array


# 시간 초과 = O(n^2)
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                continue


N = int(sys.stdin.readline())
arr = list()
for n in range(N):
    arr.append(int(sys.stdin.readline()))
# bubblesort(arr)
# newarr = mergesort(arr)
newarr = sorted(arr)
for elem in newarr:
    print(elem)