import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    a = list(map(int, input().split()))
    for i in range(1, len(a) - 2, 2):
        graph[a[0]].append((a[i], a[i + 1]))

def bfs(start):
    visit = [-1] * (v + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    m = [0, 0]

    while que:
        t = que.popleft()
        for i, j in graph[t]:
            if visit[i] == -1:
                visit[i] = visit[t] + j
                que.append(i)
                if m[0] < visit[i]:
                    m = visit[i], i
    return m

dist, node = bfs(1)
dist, node = bfs(node)
print(dist)