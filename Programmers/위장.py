from itertools import product
def solution(clothes):
    answer = 0
    kinds = {}
    for cloth in clothes:
        if cloth[1] in kinds:
            kinds[cloth[1]]+= 1
        else:
            kinds[cloth[1]] = 2
    answer = '*'.join(list(map(str,kinds.values())))
    return eval(answer)-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))