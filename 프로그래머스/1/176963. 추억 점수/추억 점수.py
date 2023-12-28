def solution(name, yearning, photo):
    answer = []
    yearn_dict = dict()

    for i in range(len(name)):
        yearn_dict[name[i]] = yearning[i]

    for i in photo:
        cnt = 0
        for j in i:
            if j in name:
                cnt += yearn_dict[j]
        answer.append(cnt)

    return answer