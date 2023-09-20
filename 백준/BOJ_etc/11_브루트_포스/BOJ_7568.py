# 덩치

n = int(input())

kg_cm = []

for _ in range(n):
    kg, cm = map(int, input().split())
    kg_cm.append((kg, cm))

# print(kg_cm)

for i in kg_cm:
    rank = 1
    for j in kg_cm:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

# https://claude-u.tistory.com/122