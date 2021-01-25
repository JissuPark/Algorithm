from sys import stdin

input = stdin.readline


def find_in_a(a, bn, idx):
    while idx < len(a) and a[idx] <= bn:
        if a[idx] == bn:
            return True, idx
        else:
            idx += 1
    return False, idx


def find_number(a, b):
    a.sort()
    idx = 0
    being = dict()
    for bn in sorted(b):
        flag, idx = find_in_a(a, bn, idx)
        if flag:
            being[bn] = 1
        else:
            being[bn] = 0
    return being


if __name__ == '__main__':
    N = int(input())
    A = input().split()
    M = int(input())
    B = input().split()
    res = find_number(A, B)
    for b in B:
        print(res[b])
