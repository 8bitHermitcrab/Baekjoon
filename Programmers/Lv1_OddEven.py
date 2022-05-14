def solution(num):
    result = ['Even', 'Odd']
    if num % 2 == 0:
        answer = result[0]
    else:
        answer = result[1]
    return answer