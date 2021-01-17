from sys import stdin

input = stdin.readline


def musical_scale(m):
    if music == sorted(music):
        return 'ascending'
    elif music == sorted(music, reverse=True):
        return 'descending'
    else:
        return 'mixed'


if __name__ == "__main__":
    music = list(map(int, input().split()))
    res = musical_scale(music)
    print(res)
