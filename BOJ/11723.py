from sys import stdin

input = stdin.readline

if __name__ == "__main__":
    T = int(input())
    s = set()
    for _ in range(T):
        inst = input().strip()
        if inst == "all":
            s = set([x for x in range(1, 21)])
        elif inst == "empty":
            s.clear()
        else:
            inst, num = inst.split()
            num = int(num)
            if inst == "add":
                s.add(num)
            elif inst == "remove":
                if num in s:
                    s.remove(num)
            elif inst == "check":
                if num in s:
                    print(1)
                else:
                    print(0)
            else:
                if num in s:
                    s.remove(num)
                else:
                    s.add(num)
