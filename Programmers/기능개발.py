from math import ceil
def solution(progresses, speeds):
    answer = []
    current = 0
    for p, s in zip(progresses, speeds):
        remain = ceil((100-p)/s)
        print(remain)
        if remain <= current:
            answer[-1] += 1
        else:
            current = remain
            answer.append(1)
    return answer