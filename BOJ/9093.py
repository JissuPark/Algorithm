import sys
input = sys.stdin.readline


def inputstr():
    return input().split()


def reversestr(s):
    ret = []
    for word in s:
        ret.append(word[::-1])
    return ret


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        string = inputstr()
        rvsstr = reversestr(string)
        print(' '.join(rvsstr))