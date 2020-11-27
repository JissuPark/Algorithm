import sys

#input
input = sys.stdin.readline
T = int(input())
array = []
#solution
for i in range(41):
    if i == 0: array.append([1,0])
    elif i == 1: array.append([0,1])
    else:
        prev1 = array[i-1]
        prev2 = array[i-2]
        array.append([prev1[0]+prev2[0], prev1[1]+prev2[1]])
    #print(f'i : {i} | {array[i]}')
#output
for _ in range(T):
    N = int(input())
    print(array[N][0], array[N][1])