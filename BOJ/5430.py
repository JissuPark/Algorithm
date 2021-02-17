from sys import stdin

input = stdin.readline


def ac(p, n, a):
    idx = 0
    if p.count('D') > n:
        return 'error'
    for pi in p:
        if pi == 'R':
            idx = 0 if idx == -1 else -1
        elif pi == 'D':
            if not a:
                return 'error'
            a.pop(idx)
    if idx == 0:
        return a
    else:
        return a[::-1]


'''
def ac(p, n, a):
    if p.count('D') > n:
        return 'error'
    for pi in p:
        if pi == 'R':
            a.reverse()
        elif pi == 'D':
            if not a:
                return 'error'
            a.pop(0)
    return a
'''

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        P = input().strip()
        N = int(input())
        array = []
        for i in input()[1:-2].split(','):
            if i.isdigit():
                array.append(int(i))
        res = ac(P, N, array)
        print(str(res).replace(', ', ','))
