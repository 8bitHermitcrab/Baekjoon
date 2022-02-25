# 최댓값

nums = [int(input()) for i in range(9)]

max_num = 0

for i in range(9):
    if nums[i] > max_num:
        max_num = nums[i]

print(max_num)
max_index = (nums.index(max_num)) + 1
print(max_index)