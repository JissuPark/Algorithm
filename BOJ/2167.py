from sys import stdin

# input
N, M = map(int, stdin.readline().split())
array = []
for _ in range(N):
    array.append(list(map(int, stdin.readline().split())))
K = int(stdin.readline())
idxs = []
for _ in range(K):
    idxs.append(stdin.readline())


# solution
def Prefixsum():
    for x in range(N):
        for y in range(M):
            if y < 1: continue
            array[x][y] += array[x][y - 1]


def Sumof2array(index):
    sumray = 0
    x1, y1, x2, y2 = map(int, index.split())
    for i in range(x1 - 1, x2):
        sumray += array[i][y2 - 1]
        if y1 - 2 > -1:
            sumray -= array[i][y1 - 2]
    return sumray


# output
Prefixsum()
#print(*array, sep='\n')
for k in range(K):
    print(Sumof2array(idxs[k]))
