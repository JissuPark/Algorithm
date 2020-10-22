def solution(d, budget):
    answer = 0
    for b in sorted(d):
        if budget >= b:
            answer += 1
            budget -= b
        else: break
    return answer