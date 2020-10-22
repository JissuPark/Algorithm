from math import gcd


def solution(w, h):
    answer = w * h

    # Drainage = gcd(h, w)
    # mass = w/Drainage*h/Drainage
    # for i in range(1, w//Drainage):
    #    mass -= int(h/w*i)*2
    # answer -= mass*Drainage

    # 기울기 = 세로/가로
    # slope = h/w
    # for i in range(w):
    #    answer += int(slope*i)*2

    return answer - (w + h - gcd(h, w))