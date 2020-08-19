'''
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하며, 한 줄로 이루어져 있다. (n ≤ 123456)
입력의 마지막에는 0이 주어진다.
'''

import sys, math
prime = [True]*246913
for q in range(2, 500):
    idx = q*2
    while idx < 246913:
        prime[idx] = False
        idx += q
for n in sys.stdin:
    n = int(n)
    if n == 0:
        exit(0)
    cnt = 0
    for idx in range(n+1, 2*n+1):
        if prime[idx]:
            cnt += 1
    print(cnt)

# 아래식으로도 풀 수는 있지만 큰수가 여러번 나오면 시간 초과가 뜸
# 미리 계산된 에라토스테네스의 체를 이용해 구하는 것이 정답
# import sys, math
# for n in sys.stdin:
#     n = int(n)
#     if n == 0:
#         exit(0)
#     cnt = n
#     for x in range(n+1, 2*n+1):
#         for y in range(2, round(math.sqrt(x))+1):
#             if x % y == 0:
#                 cnt -= 1
#                 break
#     print(cnt)
