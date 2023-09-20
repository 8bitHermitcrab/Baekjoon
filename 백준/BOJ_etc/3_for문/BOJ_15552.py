# 빠른 A+B

import sys
# sys.stdin.readline()

t = int(sys.stdin.readline())
result = []

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    c = a + b
    result.append(c)

for i in result:
    print(i)