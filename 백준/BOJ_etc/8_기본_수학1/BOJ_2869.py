# 달팽이는 올라가고 싶다

# 2

import math

a, b, v = map(int, input().split())

day_count = (v-b)/(a-b)
print(math.ceil(day_count))


'''
'https://yoonsang-it.tistory.com/9'

a, b, v = map(int, input().split())

# 1 - 시간 초과
up = 0
day_count = 0

while 1: 
    day_count += 1
    up += a
    if up == v:
        print(day_count)
        break
    up -= b
'''