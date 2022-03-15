# 좋은 친구

from sys import stdin

# n줄의 학생, k등수 차이
n, k = map(int, stdin.readline().split())
students = [0] * n
data = [0] * 21
count = 0

for rank in range(n):
    # 이름의 길이
    name = len(stdin.readline().rstrip())
    students[rank] = name
    if rank > k:
        data[students[rank - k - 1]] -= 1
    count += data[name]
    data[name] += 1
print(count)

'''
https://derekahndev.github.io/problem%20solving/boj-3078/
'''