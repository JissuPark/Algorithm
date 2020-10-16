import math
from copy import deepcopy
from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    madenum = []
    for i in range(1,len(numbers)+1):
        madenum.extend(list(map(int, list(map(''.join, permutations(numbers,i))))))
    madenum = set(madenum)
    madenum -= {0,1}
    numbers = deepcopy(madenum)
    for num in madenum:
        for divisor in range(2, int(math.sqrt(num)+1)):
            if num % divisor == 0:
                numbers.remove(num)
                break
    return len(numbers)


print(solution('17'))
print(solution('011'))