from itertools import combinations
def solution(numbers):
    answer = []
    for combi in combinations(numbers,2):
        answer.append(combi[0]+combi[1])
    return sorted(list(set(answer)))