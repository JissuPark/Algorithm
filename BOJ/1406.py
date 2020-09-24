import sys
# input
S = sys.stdin.readline().rstrip()
T = int(sys.stdin.readline())
CMDs = sys.stdin.readlines()
# solution
def editor(s, cmds):
    left = list(s)
    right = list()
    for cmd in cmds:
        cmd = cmd.rstrip()
        if cmd[0] == 'L' and left:
            right.append(left.pop())
        elif cmd[0] == 'D' and right:
            left.append(right.pop())
        elif cmd[0] == 'B' and left:
            left.pop()
        elif cmd[0] == 'P':
            left.append(cmd[-1])
    right.reverse()
    return ''.join(left+right)
#output
print(editor(S, CMDs))