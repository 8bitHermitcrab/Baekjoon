# 크기가 작은 부분문자열
def solution(t, p):
    answer = []
    
    for i in range(len(t)):
        if len(t[i:len(p)+i]) == len(p):
            answer.append(int(t[i:len(p)+i]))
    
    cnt = 0
    for i in answer:
        if i <= int(p):
            cnt += 1
    
    return cnt

print(solution("3141592", "271"))