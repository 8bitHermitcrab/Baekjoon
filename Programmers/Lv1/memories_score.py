# 추억 점수
def solution(name, yearning, photo):
    answer = []
    yearn_dict = dict()

    for i in range(len(name)):
        yearn_dict[name[i]] = yearning[i]

    # print(yearn_dict)

    for i in photo:
        cnt = 0
        # print(f'i = {i}')
        for j in i:
            # print(f'j = {j}')
            if j in name:
                cnt += yearn_dict[j]
                # print(f'cnt = {cnt}')
        answer.append(cnt)


    return answer

print(solution(["may", "kein", "kain", "radi"], 
               [5, 10, 1, 3], 
               [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))