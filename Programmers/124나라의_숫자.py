def solution(n):
    answer = ''
    if n < 3:
        return str(n)
    elif n == 3:
        return '4'
    div = 0
    res = 0
    n = n-1
    while n > 2:
        div = n // 3
        res = n % 3
        crt = 0
        if res == 0:
            crt = 1
        elif res == 1:
            crt = 2
        elif res == 2:
            crt = 4
        answer = str(crt)+answer
        n = div-1
    if div == 3:
        answer = '4'+answer
    else:
        answer = str(div)+answer
    return answer