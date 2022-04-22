# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]
# 답 : 5

# n = 5
# lost = [2, 4]
# reserve = [3]
# 답 : 4

# n = 3
# lost = [3]
# reserve = [1]
# 답 : 2

# n = 5
# lost = [3]
# reserve = [3]
# 답 = 4

'''
# 전체 학생의 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve

# 체육수업을 들을 수 있는 학생의 최대값 answer
answer = 0

# 전체 딕셔너리 = {학생번호 : 체육복 수}
n_dict = dict()
for i in range(1, n+1):
    n_dict[i] = 1

# print(n_dict)
# {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    
# 전체 딕셔너리 + 여벌 체육복 수
for i in range(len(reserve)):
    key = reserve[i]
    n_dict[key] = 2

# print(n_dict)
# {1: 1, 2: 1, 3: 2, 4: 1, 5: 1}

# 전체 딕셔너리 - 잃어버린 체육복
for i in range(len(lost)):
    key = lost[i]
    if lost == reserve:
        n_dict[key] = 0
    else:
        n_dict[key] -= 1

# print(n_dict)

# 여벌 체육복을 빌려줄 때
for key, value in n_dict.items():
    for i in range(1, n+1): # 1부터 n까지
        key = i
        if key == 1:
            # {1 : 2, 2 : 0} 일 때
            if n_dict[1] == 2 and n_dict[2] == 0:
                n_dict[1] = 1
                n_dict[2] = 1
            # {1 : 0, 2 : 2} 일 때
            elif n_dict[1] == 0 and n_dict[2] == 2:
                n_dict[1] = 1
                n_dict[2] = 1
        elif key == n:
            # {4 : 2, 5 : 0} 일 때
            if n_dict[n-1] == 2 and n_dict[n] == 0:
                n_dict[n-1] = 1
                n_dict[n] = 1
            # {4 : 0, 5 : 2} 일 때
            elif n_dict[n-1] == 0 and n_dict[n] == 2:
                n_dict[n-1] = 1
                n_dict[n] = 1
        else : # key >= 2 and key < n:
            # key = 2, 3, 4
            if n_dict[key] == 2:
                if n_dict[key - 1] == 0:
                    n_dict[key] = 1
                    n_dict[key - 1] = 1
                elif n_dict[key + 1] == 0:
                    n_dict[key] = 1
                    n_dict[key + 1] = 1
# for key, value in n_dict.items():
    if value >= 1:
        answer += 1

# print(n_dict)
print(answer)
'''


# 채점 결과
# 정확성: 75.0
# 합계: 75.0 / 100.0



n = 5
lost = [3, 4]
reserve = [2, 3]
# {1:1, 2:1, 3:1, 4:0, 5:1}
# 답 = 4


# lost 중복제거
lost_set = set(lost) - set(reserve)
# reserve 중복제거
reserve_set = set(reserve) - set(lost)

# print(lost_set)
# print(reserve_set)

answer = 0

'''
for r in reserve:
    if r not in lost:
'''

lost.sort()
reserve.sort()

# reserve 중복 제거 리스트
uniq_reserve = [r for r in reserve if r not in lost]
# lost 중복 제거 리스트
uniq_lost = [l for l in lost if l not in reserve]

print(f'uniq_reserve = {uniq_reserve}')
print(f'uniq_lost = {uniq_lost}')

# lost와 reserve 안 겹치는 학생 번호 : 2번
for r in reserve:
    m = r - 1 # 1번일 때
    p = r + 1 # 3번일 때
    if m in uniq_lost: # 1번이 잃어버렸을 때
        uniq_lost.remove(m)
    elif p in uniq_lost: # 3번이 잃어버렸을 때
        uniq_lost.remove(p)

answer = n - len(uniq_lost)
print(n - len(uniq_lost))
print(answer)

'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''

#https://velog.io/@ckr3453/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B2%B4%EC%9C%A1%EB%B3%B5