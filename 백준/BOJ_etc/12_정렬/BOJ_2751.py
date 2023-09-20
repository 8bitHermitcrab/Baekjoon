# 수 정렬하기 2

import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for data in num_list:
    print(data)

# https://leunco.tistory.com/m/71


'''
import sys

n = int(sys.stdin.readline())

num_list = []

for _ in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)

# print(num_list)

for i in range(n-1, -1, -1):
    print(num_list[i])
'''