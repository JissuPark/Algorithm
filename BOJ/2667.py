from sys import stdin

input = stdin.readline


def bfs(n, c, x, y):
    cnt = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    que = {(x, y)}
    while que:
        cx, cy = que.pop()
        c[cx][cy] = 0
        for i in range(4):
            dxi = cx + dx[i]
            dyi = cy + dy[i]
            if 0 <= dxi < n and 0 <= dyi < n and c[dxi][dyi] == 1:
                que.add((dxi, dyi))
        cnt += 1
    return cnt


def numbering_complex(n, c):
    complex_cnt = []
    for cx, row in enumerate(c):
        for cy, col in enumerate(row):
            if col == 1:
                complex_cnt.append(bfs(n, c, cx, cy))
    return len(complex_cnt), sorted(complex_cnt)


if __name__ == "__main__":
    N = int(input())
    complex = [list(map(int, list(input().strip()))) for _ in range(N)]
    cnt, res = numbering_complex(N, complex)
    print(cnt, '\n'.join(list(map(str,res))), sep='\n')
