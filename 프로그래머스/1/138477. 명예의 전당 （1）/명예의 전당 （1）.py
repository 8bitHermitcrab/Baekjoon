def solution(k, score):
    answer = []

    fame = []
    for i in score:
        if len(fame) < k:
            fame.append(i)
        
        else:
            if min(fame) < i:
                fame.remove(min(fame))
                fame.append(i)

        answer.append(min(fame))

    return answer