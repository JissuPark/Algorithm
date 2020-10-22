def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        stack = []
        for j in range(i+1,len(prices)):
            stack.append(prices[j])
            if prices[i] > prices[j]:
                break
        answer.append(len(stack))
    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3]))