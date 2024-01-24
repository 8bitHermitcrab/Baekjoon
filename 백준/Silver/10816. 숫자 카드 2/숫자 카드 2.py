# 숫자 카드 2

from sys import stdin

# 가지고 있는 숫자 카드의 개수 n
n = stdin.readline().rstrip()
cards = list(map(int, stdin.readline().split()))

# 가지고 있는 숫자 카드인지 구해야할 개수 m
m = stdin.readline().rstrip()
nums = list(map(int, stdin.readline().split()))

cnt = {}

for i in cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in nums:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')