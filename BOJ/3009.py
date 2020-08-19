'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
'''

import sys
X = list()
Y = list()
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    X.remove(x) if x in X else X.append(x)
    Y.remove(y) if y in Y else Y.append(y)
print(X[0], Y[0])