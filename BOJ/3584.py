from sys import stdin
ancient = []
def lca(c, d):
    acl = {c}
    dcl = {d}
    while c != 0 or d != 0:
        ac = ancient[c]
        dc = ancient[d]
        acl.add(ac)
        dcl.add(dc)
        if acl&dcl:
            return (acl&dcl).pop()
        c = ac
        d = dc
    return c if c == 0 else d
#input
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    ancient = [0 for _ in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, stdin.readline().split())
        # insert
        ancient[B]=A
    C, D = map(int, stdin.readline().split())
    # run solution & print output
    print(lca(C, D))
