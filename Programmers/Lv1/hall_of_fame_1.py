# 명예의 전당 (1)
def solution(k, score):
    answer = []

    fame = []
    for i in score:
        if len(fame) < k:
            fame.append(i)
        
        else:
            if min(fame) < i:
                # print(f'fame = {fame}')
                fame.remove(min(fame))
                # print(f'remove fame = {fame}')
                fame.append(i)

        answer.append(min(fame))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))

# 참고 : https://velog.io/@minmong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EB%AA%85%EC%98%88%EC%9D%98-%EC%A0%84%EB%8B%B9-Python-velog