def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    for i in range(len(s)):
        if 'y' == s[i]:
            y_cnt += 1
        elif 'Y' == s[i]:
            y_cnt += 1
        elif 'P' == s[i]:
            p_cnt += 1
        elif 'p' == s[i]:
            p_cnt += 1
    
    if y_cnt == p_cnt:
        answer = True
    else:
        answer = False

    return answer