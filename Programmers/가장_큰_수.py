# ascii로 비교하는 방식을 알았으니 자릿수를 모두 같게 만들어주는게 핵심

def solution(numbers):
    numbers = map(str, numbers)
    maxnum = sorted(numbers, key=lambda e:e*3, reverse=True)
    return int(''.join(maxnum))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))