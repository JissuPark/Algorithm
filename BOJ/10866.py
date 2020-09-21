import sys
from collections import deque
#input
T = int(sys.stdin.readline())
commands = sys.stdin.readlines()
#solution
def deck(t, cds):
    answer = []
    q = deque()
    for cd in cds:
        cd = cd.split()
        command = cd[0]
        if command == 'push_front':
            q.appendleft(cd[1])
        elif command == 'push_back':
            q.append(cd[1])
        elif command == 'pop_front':
            answer.append(q.popleft() if q else -1)
        elif command == 'pop_back':
            answer.append(q.pop() if q else -1)
        elif command == 'size':
            answer.append(len(q))
        elif command == 'empty':
            answer.append(0 if q else 1)
        elif command == 'front':
            answer.append(q[0] if q else -1)
        elif command == 'back':
            answer.append(q[-1] if q else -1)
        else:
            print("command error")
    return answer
#output
for res in deck(T, commands):
    print(res)
