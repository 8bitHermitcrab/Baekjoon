# 나머지

nums = [int(input()) for _ in range(10)]

remainder = []

for i in range(10):
    a = nums[i] % 42
    remainder.append(a)

# 중복 제거
remainder = set(remainder)
# 개수 세기
print(len(remainder))