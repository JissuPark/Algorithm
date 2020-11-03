# 오답

# def solution(number, k):
#     number = list(number)
#     for i in range(len(number)-1):
#         if k==0:
#             break
#         if number[i]<number[i+1]:
#             number[i] = ''
#             k -= 1
#     else:
#         del number[-k:]
#     return "".join(number)

# 시간초과 2개

# def solution(number, k):
#     answer = list(number)
#     number = list(number)
#     for _ in range(k):
#         for i in range(len(number)-1):
#             if number[i]<number[i+1]:
#                 number.remove(number[i])
#                 break
#         else:
#             del number[-1]
#     return "".join(number)

# 시간초과 1개 - 수정
# def solution(number, k):
#     answer = list(number)
#     number = list(number)
#     for j in range(k):
#         for i in range(len(number)-1):
#             if number[i]<number[i+1]:
#                 del number[i]
#                 break
#         else:
#             del number[-k+j:]
#             break
#     return "".join(number)

# 시간초과 2개 - while문
# def solution(number, k):
#     number = list(number)
#     loc = 0
#     while loc<(len(number)-1) and k!=0:
#         if number[loc]<number[loc+1]:
#             del number[loc]
#             loc = 0
#             k -= 1
#             continue
#         loc += 1
#     if k != 0:
#         del number[-k:]
#     return "".join(number)
def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k>0:
            stack.pop()
            k-=1
        stack.append(n)
    if k > 0:
        del stack[-k:]
    return ''.join(stack)

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
