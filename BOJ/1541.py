from sys import stdin
input = stdin.readline


def missing_parentheses(e):
    ret = 0
    e = e.replace('-', ' - ').replace('+', ' ')
    flag = 1
    for i in e.split():
        if i  == '-':
            flag = -1
            continue

        ret += int(i)*flag
    return ret


if __name__=="__main__":
    expression = input().strip()
    res = missing_parentheses(expression)
    print(res)