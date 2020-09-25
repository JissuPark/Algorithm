def solution(m, n, puddles):
    road = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    for p in puddles:
        road[p[1]][p[0]] = 0
    for x in range(1,n+1):
        for y in range(1,m+1):
            if road[x][y] == 0:
                continue
            if x == 1:
                if y == 1:
                    road[x][y] = 1
                else:
                    road[x][y] = road[x][y - 1]
            else:
                if y == 1:
                    road[x][y] = road[x - 1][y]
                else:
                    road[x][y] = road[x-1][y]+road[x][y-1]
    answer=road[n][m] % 1000000007
    return answer
#print(solution(4,3,[[2,2]]))
print(solution(3,3,[[1,2],[2,1]]))