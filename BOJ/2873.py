from sys import stdin

input = stdin.readline


def lowesthappy(h):
    _x, _y = 0, 1
    for row in range(len(h)):
        for col in range(len(h[row])):
            if row == len(h) and col == len(h[row]):
                continue
            if row == 0 and col == 0:
                continue
            if (row % 2 == 1 and col % 2 == 0) or (row % 2 == 0 and col % 2 == 1):
                if h[_x][_y] > h[row][col]:
                    _x, _y = row, col
    return _x, _y


def rollercoaster(r, c, h):
    _path = ''
    if r % 2 == 1:
        _path = ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c-1)
        return _path
    elif c % 2 == 1:
        _path = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r-1)
        return _path
    else:
        hx, hy = lowesthappy(h)
        h[hx][hy] = -1
        _path = ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (hx // 2)

        _path += ('DRUR') * (hy // 2)
        if hy % 2 == 0:
            _path += 'RD'
        else:
            _path += 'DR'
        _path += 'RURD' * ((c-1-hy)//2)

        if r-hx > 2:
            _path += 'D'
            _path += ('L' * (c - 1) + 'D' + 'R' * (c - 1) + 'D') * ((r - 1 - hx) // 2)
            _path = _path[:-1]

    return _path


if __name__ == "__main__":
    R, C = map(int, input().split())
    happies = [list(map(int, input().split())) for _ in range(R)]
    res = rollercoaster(R, C, happies)
    print(res)
