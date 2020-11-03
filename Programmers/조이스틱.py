# def solution(name):
#     answer = 0
#     stick = []
#     for n in name:
#         _n = ord(n) - 91
#         stick.append((_n % 26) if abs(_n) > (_n % 26) else abs(_n))
#     print(stick)
#     leftsum = []
#     rightsum = []
#     for i in range(1, len(stick)+1):
#         if not leftsum and stick[i % len(stick)] == 0:
#             pass
#         else:
#             leftsum.append(stick[i % len(stick)])
#         if not rightsum and stick[-i] == 0:
#             pass
#         else:
#             rightsum.append(stick[-i])
#     print(leftsum)
#     print(rightsum)
#     _left = sum(leftsum)+len(leftsum)-1
#     _right = sum(rightsum)+len(rightsum)-1
#
#     return _left if _left < _right else _right

def solution(name):
    stick = []
    for n in name:
        _n = ord(n) - 91
        stick.append(min((_n % 26) , abs(_n)))

    answer = stick[0]
    stick[0] = 0
    _stick = sum(stick)
    idx = 0
    while _stick>0:
        left = 1
        right = 1
        while stick[idx-left]<=0:
            left += 1
        while stick[idx+right]<=0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
        answer += stick[idx]
        _stick -= stick[idx]
        stick[idx] = 0
    return answer
