def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        s = ""
        for i in skill_tree:
            if i in skill:
                s += i
        if skill[:len(s)] == s:
            answer += 1

    return answer