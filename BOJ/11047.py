import sys

input = sys.stdin.readline


def coin0(price, coins):
    count = 0
    for coin in reversed(coins):
        if price >= coin:
            quotient = (price // coin)
            price -= quotient * coin
            count += quotient
    return count


if __name__ == '__main__':
    N, K = map(int, input().split())
    values = [int(input()) for _ in range(N)]
    mincnt = coin0(K, values)
    print(mincnt)
