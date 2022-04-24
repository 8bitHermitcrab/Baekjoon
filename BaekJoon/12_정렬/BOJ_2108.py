# 통계학

import sys
# from collections import Counter

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))
# print(nums)

# 산술평균
print(round(sum(nums) / n))

# 중앙값
nums.sort()
print(nums[int((n-1)/2)])

# 최빈값
counts = dict()
for i in range(1, n+1):
    counts[i] = []

max_count = 1
count = 1

for j in range(1, n):
    if nums[j] == nums[j-1]:
        count += 1
    else:
        counts[count].append(nums[j-1])
        if max_count < count:
            max_count = count
        count = 1
    if j == n-1:
        counts[count].append(nums[j])
        if max_count < count:
            max_count = count

if n == 1:
    counts[1].append(nums[0])

counts[max_count].sort()
if len(counts[max_count]) == 1:
    print(counts[max_count][0])
else:
    print(counts[max_count][1])

# 범위
print(nums[-1] - nums[0])

# https://velog.io/@jaenny/%EB%B0%B1%EC%A4%80-2108-%ED%86%B5%EA%B3%84%ED%95%99-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC