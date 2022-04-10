# 수 정렬하기 3

import sys

n = int(sys.stdin.readline())

check_list = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    check_list[num] = check_list[num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)



'''
import sys

n = int(sys.stdin.readline())
num_dict = {} 

for _ in range(n):
    num = int(sys.stdin.readline())

    if num not in num_dict.keys():
        num_dict[num] = 1
    else:
        num_dict[num] = num_dict[num] + 1

print(f'num_dict = {num_dict}')
sorted_dict = sorted(num_dict.items())
print(f'sorted_dict = {sorted_dict}')

for i in range(len(sorted_dict)):
    print(f'sorted_dict[i][1] = {sorted_dict[i][1]}')
    for j in range(sorted_dict[i][1]):
        print(f'sorted_dict[i][0] = {sorted_dict[i][0]}')

# https://somjang.tistory.com/entry/Mxmxmxm
'''