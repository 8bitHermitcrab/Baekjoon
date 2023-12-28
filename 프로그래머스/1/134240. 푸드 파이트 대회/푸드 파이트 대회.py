def solution(food):
    answer = ''

    for i in range(1, len(food)):
        if food[i] % 2 == 0:
            answer = answer + str(str(i) * (food[i] // 2))
        else:
            answer = answer + str(i) * ((food[i] - 1) // 2)

    return answer + '0' + answer[::-1]