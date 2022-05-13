# 트럭

import sys

n = int(sys.stdin.readline())

asp_list = []
for i in range(n):
# 제안a, 신차 크기s, 차량1대 p원
    asp = list(map(int, sys.stdin.readline().split()))
    asp_list.append(asp)
# [[a, s, p], [a, s, p]]

# 시나리오 개수
M = int(sys.stdin.readline())

new_s_list = list(map(int, sys.stdin.readline().split()))

# print(new_s_list)
# print(asp)

answer = -1
for i in range(len(new_s_list)+1):
    if new_s_list[i] < new_s_list[i+1]:
        answer.append(new_s_list[i])

# https://softeer.ai/practice/formCodeEditor.do
