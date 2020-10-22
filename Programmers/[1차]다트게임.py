def solution(dartResult):
    answer = []
    temp = ''
    for dart in dartResult:
        if dart == 'S':
            answer.append(int(temp))
            temp = ''
        elif dart == 'D':
            answer.append(int(temp)**2)
            temp = ''
        elif dart == 'T':
            answer.append(int(temp)**3)
            temp = ''
        elif dart == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif dart == '#':
            answer[-1] *= -1
        else:
            temp += dart
    return sum(answer)