def solution(s):
    answer = ''
    s_list = s.split()
    s_list_int = list(map(int, s_list))
    s_list.sort()
    answer = str(min(s_list_int)) + ' ' + str(max(s_list_int))
    return answer