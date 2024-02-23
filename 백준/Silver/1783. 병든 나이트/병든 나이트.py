import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = 0

if n == 1:
    result = 1
elif n == 2:
    if m <= 6:
        result = (m+1) // 2
    else:
        result = 4
elif n >= 3:
    if m <= 6:
        result = min(4, m)
    else:
        result = m - 2

print(result)