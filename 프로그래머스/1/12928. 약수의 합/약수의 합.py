def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n != 1:
            if n % i == 0:
                answer += i
            else:
                continue
        else:
            answer = 1
    return answer