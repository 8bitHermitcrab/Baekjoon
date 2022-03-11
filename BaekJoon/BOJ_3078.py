'런타임 에러'
# 좋은 친구

from collections import deque

# n명, 등수 k차이
n, k = map(int, input().split())
# 이름의 길이 리스트
name_len = [len(input()) for _ in range(n)]
# 좋은 친구 수
g_f_count = 0
# 등수 리스트
score_list = [deque() for _ in range(21)]

# i: 등수 - 1, j: 이름 길이
for i, j in enumerate(name_len):
    # 큐[0]과 현재 학생의 등수가 k 이상 차이나면 popleft()
    while score_list[j] and i - score_list[j][0] > k:
        score_list.popleft()
    # 큐 안에 있는 등수의 학생들은 현재 학생과 좋은 친구
    # 큐 안의 원소 수만큼 g_f_count 증가
    if score_list[j]:
        g_f_count += len(score_list[j])
    # 큐에 현재 학생 append
    score_list[j].append(i)

print(g_f_count)



'''
https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-3078%EB%B2%88-%EC%A2%8B%EC%9D%80-%EC%B9%9C%EA%B5%ACPython
'''