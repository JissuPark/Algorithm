from sys import stdin

input = stdin.readline

# 0을 기준으로 나눠 복잡해진 코드
'''
def tienumber(p, m):
    maxsum = 0
    p.sort()
    m.sort(reverse=True)
    while len(p) > 1:
        a, b = p.pop(), p.pop()
        maxsum += a * b if a * b > a + b else a + b
    while len(m) > 1:
        temp = m.pop() * m.pop()
        maxsum += temp
    if p: maxsum += sum(p)
    if m: maxsum += sum(m) if not zero else 0
    total = sum(p) + sum(m)
    return maxsum if maxsum > total else total


if __name__ == '__main__':
    N = int(input())
    plus, minus, zero = [], [], False
    for _ in range(N):
        num = int(input())
        if num > 0:
            plus.append(num)
        elif num == 0:
            zero = True
        else:
            minus.append(num)
    res = tienumber(plus, minus)
    print(res)
'''


# 1을 기준으로 나눠 최적화한 코드
def tienumber(p, m, o):
    maxsum = 0

    p.sort()
    m.sort(reverse=True)
    while len(p) > 1:
        maxsum += p.pop() * p.pop()
    while len(m) > 1:
        maxsum += m.pop() * m.pop()

    if p: maxsum += sum(p)
    if m: maxsum += sum(m)
    maxsum += sum(o)

    return maxsum


if __name__ == '__main__':
    N = int(input())
    plus, minus, ones = [], [], []
    for _ in range(N):
        num = int(input())
        if num > 1:
            plus.append(num)
        elif num < 1:
            minus.append(num)
        else:
            ones.append(num)
    res = tienumber(plus, minus, ones)
    print(res)
