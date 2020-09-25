def solution(n, edge):
    weight = [50001] * (n + 1)
    linked = [[] for _ in range(n + 1)]
    for e1, e2 in edge:
        linked[e1].append(e2)
        linked[e2].append(e1)
    stack = [1]
    weight[0] = 0
    weight[1] = 0
    while stack:
        idx = stack.pop(0)
        for i in linked[idx]:
            if weight[idx] + 1 < weight[i]:
                weight[i] = weight[idx] + 1
                stack.append(i)
            else:
                continue
    maxweight = max(weight)
    return weight.count(maxweight)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
