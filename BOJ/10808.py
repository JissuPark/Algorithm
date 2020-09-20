import sys
#input
String = sys.stdin.readline()
#solution
def alphacnt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for apb in alphabet:
        answer += str(s.count(apb))
        answer += ' '
    return answer
#output
print(alphacnt(String).strip())