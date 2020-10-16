import sys
from itertools import product


def remocon(ch, broken):
    currentch = 100
    validch = [str(i) for i in range(10)]
    directch = abs(currentch - ch)
    closech = directch
    for bt in broken:
        validch.remove(bt)
    if len(validch) == 0:
        return directch
    for i in range(1000001):
        isbroken = False
        for num in str(i):
            if num in broken:
                isbroken = True
                break
        if isbroken is not True and closech > abs(i-ch)+len(str(i)):
            closech = abs(i - ch)+len(str(i))
    # for idx in range(-1, 2):
    #     if len(str(ch)) + idx < 1:
    #         continue
    #     procombi = list(map(''.join, product(validch, repeat=len(str(ch)) + idx)))
    #     for combi in procombi:
    #         combinum = ''.join(combi)
    #         resnum = abs(ch - int(combinum))
    #         resnum += len(combinum)
    #         if resnum < closech:
    #             closech = resnum
    #     del procombi
    return closech


# input
N = int(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline().rstrip())
broken_bt = []
if T != 0:
    broken_bt = list(map(str, sys.stdin.readline().rstrip().split()))
# output
print(remocon(N, broken_bt))
