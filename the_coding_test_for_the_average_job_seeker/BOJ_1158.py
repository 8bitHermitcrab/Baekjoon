# 요세푸스 문제

from collections import deque

n, k = map(int, input().split())

que = deque([i+1 for i in range(n)])
index = 0
print('<', end='')
for i in range(n - 1):
    for _ in range(k - 1):
        que.append(que.popleft())
    print(f'{que.popleft()}, ', end='')
print(f'{que.popleft()}>', end='')


# https://velog.io/@delicate1290/%EB%B0%B1%EC%A4%80-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4-%EB%AC%B8%EC%A0%9C-1158%EB%B2%88
