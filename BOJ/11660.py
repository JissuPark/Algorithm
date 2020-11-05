from sys import stdin

# input
N, M = map(int, stdin.readline().split())
array = []
for _ in range(N):
    array.append(list(map(int, stdin.readline().split())))


# solution
def Prefixsum():
    for x in range(N):
        vertisum = 0
        for y in range(N):
            vertisum += array[x][y]
            if x == 0 and y == 0:
                continue
            elif y == 0:
                array[x][y] += array[x - 1][y]
            elif x == 0:
                array[x][y] = vertisum
            else:
                array[x][y] = vertisum + array[x - 1][y]


def Sumof2array(index):
    x1, y1, x2, y2 = map(int, index.split())
    sumray = array[x2 - 1][y2 - 1]
    if x1 > 1: sumray -= array[x1 - 2][y2 - 1]
    if y1 > 1: sumray -= array[x2 - 1][y1 - 2]
    if x1 > 1 and y1 > 1: sumray += array[x1 - 2][y1 - 2]
    return sumray


# output
Prefixsum()
# print(*array, sep='\n')
for k in range(M):
    print(Sumof2array(stdin.readline()))
