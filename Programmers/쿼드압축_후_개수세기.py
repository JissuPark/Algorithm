import numpy as np

def solution(arr):
    def quadtree(x, y, n):
        nonlocal arr
        if n == 1:
            return [arr[x][y]]
        s1 = quadtree(x, y, n // 2)
        s2 = quadtree(x + n // 2, y, n // 2)
        s3 = quadtree(x, y + n // 2, n // 2)
        s4 = quadtree(x + n // 2, y + n // 2, n // 2)
        square = np.array(s1 + s2 + s3 + s4)
        if np.all(square == 1):
            return [1]
        elif np.all(square == 0):
            return [0]
        else:
            return square

    answer = quadtree(0, 0, len(arr))
    return [answer.count(0), answer.count(1)]

print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))