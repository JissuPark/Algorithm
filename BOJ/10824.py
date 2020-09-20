import sys
#input
A, B, C, D = sys.stdin.readline().split()
#solution
def fournum(a,b,c,d):
    fst = int(a+b)
    snd = int(c+d)
    return fst+snd
#output
print(fournum(A,B,C,D))