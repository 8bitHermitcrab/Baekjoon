# 터렛

import math

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 두 원의 거리 (원의 방정식)
    if d == 0 and r1 == r2: # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == d or r1+r2 == d: # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < d < (r1+r2): # 두 원이 서로 다른 두 점에서 만날 때
        print(2)
    else:
        print(0)

# https://ooyoung.tistory.com/111