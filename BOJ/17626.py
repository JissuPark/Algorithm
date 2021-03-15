from sys import stdin, setrecursionlimit

# setrecursionlimit(10000)
input = stdin.readline


def four_squares(n):
    if (n ** 0.5).is_integer():
        return 1
    for i in range(1, int(n ** 0.5) + 1):
        if n < i ** 2:
            break
        if ((n - i ** 2) ** 0.5).is_integer():
            return 2
    for i in range(1, int(n**0.5) + 1):
        if n < i ** 2:
            break
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if n < i ** 2 + j ** 2:
                break
            if ((n - i ** 2 - j ** 2) ** 0.5).is_integer():
                return 3
    return 4


'''
# PyPy3 : 통과
def four_squares(n):
    if (n ** 0.5).is_integer():
        return 1
    for i in range(2, n + 1):
        _min = 1e9
        if n > i * i and ((n - i * i) ** 0.5).is_integer():
            return 2
        for j in range(1, int(i ** 0.5) + 1):
            _min = min(_min, DP[i - j * j] + 1)
        DP.append(_min)
    return DP[n]
'''

'''
# DP : 시간초과 ? 왜 
def four_squares(n):
    DP[1] = 1
    for i in range(2, n + 1):
        for j in range(1, int(i ** 0.5) + 1):
            DP[i] = min(DP[i], DP[i - j * j] + 1)
    return DP[n]
'''

'''
# 재귀 : 시간초과 
def four_squares(n):
    sqrt = n ** 0.5
    if sqrt.is_integer():
        return 1
    tmp = []
    for i in range(int(sqrt), 0, -1):
        tmp.append(four_squares(n-(i**2))+1)
    tmp.sort()
    return tmp[0]
'''
'''
# 그리디 : 시간초과
def four_squares(n):
    print(n, int(n**0.5),int(n**0.5)**2, n-int(n**0.5)**2)
    if n == 1:
        return 1
    sqrt = n**0.5
    if sqrt.is_integer():
        return 1
    return four_squares(n-int(sqrt)**2)+1
'''

if __name__ == "__main__":
    N = int(input())
    res = four_squares(N)
    print(res)
