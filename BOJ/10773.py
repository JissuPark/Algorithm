from sys import stdin
input = stdin.readline


def zero(m):
    stack = []
    for n in m:
        if n == 0:
            stack.pop()
        else:
            stack.append(n)
    return sum(stack)


if __name__ == '__main__':
    K = int(input())
    money = [int(input()) for _ in range(K)]
    res = zero(money)
    print(res)