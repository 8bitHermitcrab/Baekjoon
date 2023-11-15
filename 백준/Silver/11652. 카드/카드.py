n = int(input())

num_dict = {}
for i in range(n):
    num = int(input())

    if num_dict.get(num, 0):
        num_dict[num] += 1
    else:
        num_dict[num] = 1

num_dict = sorted(num_dict.items(), key = lambda x: (-x[1], x[0]))

print(num_dict[0][0])