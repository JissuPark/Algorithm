def solution(board):
    answer = board[0][0]
    n = len(board)
    m = len(board[0])
    for row in range(n):
        for col in range(m):
            if board[row][col] == 0 or row == 0 or col == 0:
                continue
            else:
                minlen = min(board[row-1][col-1], board[row-1][col])
                minlen = min(board[row][col-1], minlen)
                board[row][col]=minlen+1
                answer = max(answer, board[row][col]**2)
                #print(*board, sep='\n')
                #print("=======")
    return answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))

import numpy as np

#시간초과
def solution(board):
    answer = 0
    b = np.array(board)
    n = len(board)
    m = len(board[0])
    for row in range(n):
        for col in range(m):
            if board[row][col] == 0:
                continue
            depth = 0

            def bfs(d):
                nonlocal row, col, n, m
                if row + d >= n or col + d >= m:
                    return d
                if np.all(b[row + d, col:col + d]) == 1 and \
                        np.all(b[row:row + d, col]) == 1:
                    return bfs(d + 1)
                return d

            depth = bfs(depth)
            answer = max(answer, depth * depth)

    return answer