'''
세 정수 A, B, C가 주어진다.
이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

두 가지 방법이 생각나는데
1. list로 받아서 sort함
2. 두 번의 비교를 통해서 가운데 값을 탐색
'''

# 1번 코드
a = list(map(int, input().split()))
a.sort()
print(a[1])