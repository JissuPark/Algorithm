from sys import stdin
input = stdin.readline


def hashing(p):
    ret = 0
    r, m = 31, 1234567891
    for i, q in enumerate(p):
         ret = (ret + (ord(q)-96)*(r**i)) % m
    return ret
# def hashing(p):
#     ret = 0
#     r, m = 31, 1234567891
#     for i, q in enumerate(p):
#          ret += (ord(q)-96)*(r**i) % m
#     return ret


if __name__ == "__main__":
    L = int(input())
    plain_text = input().strip()
    res = hashing(plain_text)
    print(res)