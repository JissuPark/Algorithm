import sys

input = sys.stdin.readline


def bitcheck(b):
    global checked
    bit = (1 << b[0])
    print(f'start & end = {bin(bit)}({b[0]})&{bin(1 << (b[1]))}({b[1]})')
    for _ in range(b[1] - b[0]):
        if checked & bit:
            return False
        bit = bit << 1
    bit = bit >> 1
    for _ in range(b[1] - b[0]):
        checked = checked | bit
        bit = bit >> 1
    return True


def assignroom(m):
    cnt = 0
    last = 0
    m.sort(key=lambda time: (time[1], time[0]))
    for meet in m:
        if last <= meet[0]:
            cnt += 1
            last = meet[1]
    return cnt


if __name__ == "__main__":
    N = int(input())
    # checked = 0b0
    meeting = [list(map(int, input().split())) for _ in range(N)]
    res = assignroom(meeting)
    print(res)
