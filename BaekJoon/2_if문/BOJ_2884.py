# 알람 시계

h, m = map(int, input().split())

m = m - 45
clock = 60

if m < 0:
    m = clock + m
    h -= 1
    if h < 0:
        h = h + 24

print(h, m)