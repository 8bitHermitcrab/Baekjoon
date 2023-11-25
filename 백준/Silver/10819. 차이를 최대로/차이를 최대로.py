from itertools import permutations

n = int(input())

nums = list(map(int, input().split()))

per = permutations(nums)

answer = 0

for i in per:
    s = 0
    for j in range(len(i) - 1):
        s += abs(i[j] - i[j + 1])
    if s > answer:
        answer = s

print(answer)