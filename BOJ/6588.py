import sys

input = sys.stdin.readline


def valideven(n):
    for odd in range(3, n//2+1):
        if check[odd] and check[n-odd]:
            return f'{n} = {odd} + {n - odd}'
    else:
        return "Goldbach's conjecture is wrong"


if __name__ == "__main__":
    check = [False]*3 + [True] * 1000000
    for i in range(2, 1000001):
        if check[i]:
            for j in range(i * 2, 1000000, i):
                check[j] = False
    while True:
        even = int(input())
        if even == 0: break
        print(valideven(even))
    # for aa in range(6,1000000, 2):
    #     print(valideven(aa))