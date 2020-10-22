from collections import deque
def solution(priorities, location):
    answer = 1
    locates = deque((i,x) for i,x in enumerate(priorities))
    while priorities:
        paper = locates.popleft()
        if locates and paper[1] < max(locates, key=lambda x:x[1])[1]:
            locates.append(paper)
        else:
            if paper[0] == location:
                break
            answer += 1
    return answer
def solution(priorities, location):
    answer = 1
    locates = [i for i in range(len(priorities))]
    while priorities:
        paper = priorities.pop(0)
        loc = locates.pop(0)
        if priorities and paper < max(priorities):
            priorities.append(paper)
            locates.append(loc)
        else:
            if loc == location:
                break
            answer += 1
    return answer
print(solution([2, 1, 3, 2],2))
