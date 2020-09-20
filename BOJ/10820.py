import sys
#input
String = sys.stdin.readlines()
#solution
def stranalyze(s):
    answer = []
    for line in s:
        upper = 0
        lower = 0
        number = 0
        space = 0
        for char in line[:-1]:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isdigit():
                number += 1
            else:
                space += 1
        answer.append([lower, upper, number, space])
    return answer
#output
for a in stranalyze(String):
    print(a[0],a[1],a[2],a[3], sep=' ', end='\n')