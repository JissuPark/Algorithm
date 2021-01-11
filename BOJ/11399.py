from sys import stdin
input = stdin.readline


def ATM(p):
    _total = 0
    for i, pi in enumerate(sorted(p, reverse=True)):
        _total += (pi*(i+1))
        #print(f'pi = {pi} => total = {_total}')
    return _total


if __name__ == "__main__":
    N = int(input())
    _time = list(map(int, input().split()))
    res = ATM(_time)
    print(res)