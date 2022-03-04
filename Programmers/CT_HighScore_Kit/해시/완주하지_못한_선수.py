participant = list(input().split())
completion = list(input().split())

participant.sort()
completion.sort()

for p, c in zip(participant, completion):
    if p != c:
        p

print(participant[-1])

# ===========================================
def solution(participant, completion):
    # participant : 참가자, completion : 완주자, return : 미완주자
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

# ==========================================



""" def solution(participant, completion):
    # participant : 참가자, completion : 완주자, return : 미완주자
    participant = []
    completion = []
    # participant - completion
    # p_sub_c = [i for i in participant if not in completion]
    # return
    answer = ''
    # answer = participant - completion
    answer = p_sub_c

    return answer """


# participant : 참가자, completion : 완주자, return : 미완주자
participant = list(input().split())
completion = list(input().split())
# participant - completion
p_sub_c = [i for i in participant if i not in completion]
set_part = set(participant)
p_sub_s = [i for i in participant if i not in set_part]

# return
# answer = []
""" 
# answer = participant - completion
for i in set_part:
    answer = participant.pop(i)

for i in answer:
    print(i)
 """
'''
hap_p_c = participant + completion
for i in range(len(hap_p_c)):
    answer = participant.pop(hap_p_c[i])
'''

""" # 완주시 카운트 +1, 완주자는 2, 미완주자는 1
count_dict = dict()
count_list = []
count = 0

for i in range(len(participant)):
    for j in range(len(completion)):
        if participant[i] == completion[j]:
            count += 1
            count_list.append(count)
        else:
            continue

    count_dict[participant[i]] = count[i] 

print(count_dict)
"""

'''
answer = {}
for i in participant:
    answer[i] = answer.get(i, 0)
    print(f'answer[{i}] = {answer[i]}')
    print(f'answer.get({i}, 0) = {answer.get(i, 0)}')
    answer[i] = answer.get(i, 0) + 1
    print(f'answer[i] + 1 = {answer[i]}')

    # answer[leo] = 0
    # answer.get(key, 키값이 없을 경우 가져올 디폴트값)
    # answer.get(leo, 0) = 0

for j in completion:
    answer[j] -= 1
    # print(f'answer[{j}] = {answer[j]}')
    # answer[kiki] = -1
for k in answer:
    if answer[k]:
        print(f'answer[{k}] = {answer[k]}')
        # answer[kiki] = -1
        # return k


https://hjp845.tistory.com/54

https://mungto.tistory.com/193

https://jione-e.tistory.com/44
'''