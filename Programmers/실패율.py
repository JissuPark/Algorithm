def solution(N, stages):
    answer = []
    remain = len(stages)
    for i in range(1, N+1):
        if remain < 1:
            answer.append((i, 0))
            continue
        answer.append((i,stages.count(i)/remain))
        remain -= stages.count(i)
    return [idx[0] for idx in sorted(answer, key=lambda x:(x[1], -x[0]),reverse=True )]