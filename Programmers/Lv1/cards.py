# 카드 뭉치
def solution(cards1, cards2, goal):
    answer = []

    i, j = 0, 0
    for word in goal:
        if i < len(cards1) and word == cards1[i]:
            answer.append(cards1[i])
            # print(f'card1 answer = {answer}')
            i += 1
    
        if j < len(cards2) and word == cards2[j]:
            answer.append(cards2[j])
            # print(f'card2 answer = {answer}')
            j += 1
    
    if answer == goal:
        return 'Yes'
    
    else:
        return 'No'

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

# 참고 : https://velog.io/@ggb05224/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%EB%93%9C-%EB%AD%89%EC%B9%98-python