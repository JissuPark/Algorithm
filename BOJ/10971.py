import sys

def TSP(cnt, city):
    expenses = []
    stack = []
    price = 0
    next = 0
    stack.append(0)
    while stack:
        if cnt == 1 and city[next][0] > 0:
            expenses.append(price)
            price = 0
            cnt = len(city)
        next = stack.pop()
        for i in range(len(city)):
            if city[next][i]:
                stack.append(i)
        price += city[next][stack[-1]]
        cnt -= 1
    return sorted(expenses[0])


#input
N = int(sys.stdin.readline())
cities = []
for n in range(N):
    cities.append(list(map(int, sys.stdin.readline().split())))
#output
print(TSP(N, cities))
