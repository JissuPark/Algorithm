class MinHeap:

    def __init__(self):
        self.que = [0]

    def insert(self, x):
        # 맨 마지막에 원소 추가
        self.que.append(x)
        # 부모보다 클때까지 이동
        idx = len(self.que) - 1  # 현재 인덱스
        while 1 < idx:
            # 부모와 비교 (부모 : 현재 // 2)
            if self.que[idx] < self.que[idx // 2]:  # 부모가 더 크면 swap
                self.swap(idx, idx // 2)
                idx = idx // 2
            else:  # 부모가 더 작으면 끝
                break

    def delete(self):
        # 배열이 비었을때
        if len(self.que) == 1:
            return 0
        # 맨 처음이랑 맨 마지막 swap
        self.swap(1, -1)
        # 맨 마지막이 최소이므로 pop
        _min = self.que.pop()
        # 재정렬
        self.sort()
        return _min

    def swap(self, i1, i2):
        self.que[i1], self.que[i2] = self.que[i2], self.que[i1]

    def sort(self):
        _idx = 1

        while len(self.que) > 1:
            _next = _idx
            if _idx * 2 < len(self.que) and self.que[_idx * 2] < self.que[_next]:
                _next = _idx * 2

            if _idx * 2 + 1 < len(self.que) and self.que[_idx * 2 + 1] < self.que[_next]:
                _next = _idx * 2 + 1

            if _next != _idx:
                self.swap(_idx, _next)
                _idx = _next

            else:
                break