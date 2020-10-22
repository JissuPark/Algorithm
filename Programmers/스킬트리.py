def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        check = ''
        for branch in tree:
            if branch not in skill:
                continue
            check+=branch
        if skill.find(check)==0:
            answer += 1
    return answer