import sys

input = sys.stdin.readline


def stackcheck(n):
    stack = []
    maxnum = 0
    ret = []
    for _ in range(n):
        num = int(input())

        if not stack:
            for i in range(maxnum + 1, num + 1):
                stack.append(i)
                ret.append('+')
            stack.pop()
            ret.append('-')
        elif stack[-1] == num:
            stack.pop()
            ret.append('-')
        elif stack[-1] < num:
            for i in range(maxnum + 1, num + 1):
                stack.append(i)
                ret.append('+')
            stack.pop()
            ret.append('-')
        else:
            return []
        maxnum = max(maxnum, num)
    return ret


if __name__ == "__main__":
    N = int(input())
    result = stackcheck(N)
    if result:
        print('\n'.join(result))
    else:
        print('NO')
