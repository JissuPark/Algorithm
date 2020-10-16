def solution(n):
    answer = ''
    div = 0
    res = 0
    mul = 1
    intanswer = 0 if n > 2 else n
    while n>=3:
        div = n//3
        res = n%3
        n = div
        answer = str(res)+answer
    answer = str(div)+answer
    for i in answer:
        intanswer += mul*int(i)
        mul *= 3
    return intanswer