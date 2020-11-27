import sys
input = sys.stdin.readline


def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i == 0 and b%i == 0:
            return i


def lcm(a,b,g):
    return a*b//g


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A,B = map(int, input().split())
        GCD = gcd(A,B)
        LCM = lcm(A,B,GCD)
        print(LCM)