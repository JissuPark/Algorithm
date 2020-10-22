from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    sum_truck = truck_weights[0]
    onbridge = deque([0]*bridge_length)
    onbridge.appendleft(truck_weights.pop(0))
    while sum_truck!=0:
        if len(onbridge) > bridge_length:
            temp = onbridge.pop()
            if temp!=0:
                sum_truck -= temp
        if truck_weights:
            this_truck = truck_weights[0]
            if sum_truck-onbridge[-1] + this_truck <= weight:
                onbridge.appendleft(truck_weights.pop(0))
                sum_truck += this_truck
            else:
                onbridge.appendleft(0)
        else:
            onbridge.appendleft(0)

        time += 1
    return time

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])