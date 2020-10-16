def solution(numbers, target):
    len_t = len(numbers)
    cnt = 0
    res = 0
    def dfs(depth):
        nonlocal res,cnt
        if depth==len_t:
            if res == target:
                cnt += 1
            return
        res += numbers[depth]
        dfs(depth+1)
        res -= numbers[depth]*2
        dfs(depth+1)
        res += numbers[depth]
    dfs(0)
    return cnt