from sys import stdin

input = stdin.readline


def valid_number(n):
    return sum(map(lambda x: x ** 2, n)) % 10


if __name__ == "__main__":
    unique_number = list(map(int, input().split()))
    res = valid_number(unique_number)
    print(res)
