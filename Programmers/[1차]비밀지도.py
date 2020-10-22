def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        num = a | b
        answer.append((bin(num)[2:].zfill(n).replace('1', '#').replace('0', ' ')))
    return answer

# rjust