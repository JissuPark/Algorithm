import sys
input = sys.stdin.readline


def drainage30(num):
    bigone = -1
    # 0이 없으면 30의 배수가 안됨
    if '0' not in num:
        return -1
    # 전부 더해서 3의 배수인지 확인
    sumnum = sum(map(int, num))
    if sumnum % 3 == 0:
        bigone = ''.join(sorted(num, reverse=True))
    # 맞다면 새로운 값이, 아니라면 원래 있던 -1이 반환
    return bigone


if __name__ == "__main__":
    N = input().strip()
    res = drainage30(N)
    print(res)