# 과일 장수

def solution(k, m, score):
    answer = 0

    score.sort(reverse=True)
    # print(score)
    
    for i in range(len(score)):
        if (i + 1) % m == 0:
            # print(f'i = {i}')
            answer += score[i] * m
            # print(f'score[{i}] = {score[i]}')

    return answer

print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

# 참고1 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%BC%EC%9D%BC-%EC%9E%A5%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
# 참고2 : https://americanoisice.tistory.com/133