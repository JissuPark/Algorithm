import sys
#input
S = sys.stdin.readline()
#solution
def rot13(str):
    answer = ""
    for s in str:
        if ord(s)>64 and ord(s)<91:
            answer += chr(65+(ord(s)-65+13)%26)
        elif ord(s)>96 and ord(s)<123:
            answer += chr(97+(ord(s)-97+13)%26)
        else:
            answer += s
    return answer
#output
print(rot13(S))