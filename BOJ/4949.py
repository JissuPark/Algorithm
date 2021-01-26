from sys import stdin

input = stdin.readline


def balanced_world(s):
    stack = []
    for arg in s:
        if arg == '(' or arg == '[':
            stack.append(arg)
        elif arg == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'no'
        elif arg == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return 'no'
    if stack:
        return 'no'
    return 'yes'


if __name__ == "__main__":
    while True:
        string = input().rstrip()
        if string == '.':
            break
        res = balanced_world(string)
        print(res)
