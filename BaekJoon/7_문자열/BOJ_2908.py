# 상수

num1, num2 = map(int, input().split())

num1 = str(num1)
num1 = int(num1[::-1])
num2 = str(num2)
num2 = int(num2[::-1])

nums_list = []
nums_list.append(num1)
nums_list.append(num2)

print(max(nums_list))

'''
# for num in nums:
#     a = num[::-1]
#     new_nums.append(int(a))

print(nums.reverse())

# print(max(new_nums))
'''