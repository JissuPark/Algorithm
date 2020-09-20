import sys
#input
S = sys.stdin.readline().strip()
#solution
def suffixarray(s):
    answer = []
    for i in range(len(s)):
        answer.append(s[i:])
    return sorted(answer)
#output
print('\n'.join(suffixarray(S)))