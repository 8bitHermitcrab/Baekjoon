def solution(cards1, cards2, goal):
    answer = []

    i, j = 0, 0
    for word in goal:
        if i < len(cards1) and word == cards1[i]:
            answer.append(cards1[i])
            i += 1
    
        if j < len(cards2) and word == cards2[j]:
            answer.append(cards2[j])
            j += 1
    
    if answer == goal:
        return 'Yes'
    
    else:
        return 'No'