'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
'''

import sys
import itertools
N = int(sys.stdin.readline())
cnt = 0
for n in range(N):
    word = sys.stdin.readline().strip()
    alpha = ''.join(a for a, _ in itertools.groupby(word))
    check = dict()
    for a in alpha:
        if a in check:
            cnt -= 1
            break
        else:
            check[a] = True
    cnt += 1
print(cnt)

# 내 코드는 연속되는 문자를 지우고 한글자씩 사전에 저장하면서 이미 있는 것이 나오면 빼서
# 그룹 문자가 아닌 것을 제외하는 식인데
# sorted의 key를 사용해 아래와 같이 그룹문자인 것을 고를 수 도 있다.
for n in range(N):
    word = sys.stdin.readline().strip()
    if list(word) is sorted(word, key=word.find):
        cnt += 1
print(cnt)