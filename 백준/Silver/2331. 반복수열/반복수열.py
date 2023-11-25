a, p = map(int, input().split())

nums = [a]

while True:
    temp = 0

    for i in str(nums[-1]):
        temp += int(i) ** p

    if temp in nums:
        break

    nums.append(temp)

print(nums.index(temp))