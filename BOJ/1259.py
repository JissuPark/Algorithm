from sys import stdin

input = stdin.readline


def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return 'no'
    return 'yes'


if __name__ == "__main__":
    while True:
        number = input().strip()
        if number == '0':
            break
        res = palindrome(number)
        print(res)
