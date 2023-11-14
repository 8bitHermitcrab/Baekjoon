n = int(input())

num_list = [list(input().split()) for _ in range(n)]

num_list.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in num_list:
    print(i[0])