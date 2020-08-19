'''
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
이 아파트에 거주를 하려면 조건이 있는데, “
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
첫 번째 줄에 Test case의 수 T가 주어진다.
그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)

solve)
2차원 배열을 선언하여 미리 연산을 해놓고 바로 출력함
미리 선언하는 부분은 home[x][y]를 연산하는 경우,
home[x][y-1]가 이전 호까지 사는 사람의 수 이므로
home[x-1][y]에 사는 사람수만 더해주면 되므로 연산을 빠르게 할 수 있다.
'''

import sys
home = [[0 for col in range(14)] for row in range(15)]
for row in range(15):
    for col in range(14):
        if row == 0:
            home[row][col] = col+1
        elif col == 0:
            home[row][col] = 1
        else:
            home[row][col] = home[row][col-1] + home[row-1][col]
T = int(sys.stdin.readline())
for t in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(home[k][n-1])