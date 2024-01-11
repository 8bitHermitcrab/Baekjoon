import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize

def dfs(i, j):
    global cnt
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if array[i][j] == 1:
        array[i][j] = cnt
        for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx = x + i
            ny = y + j
            dfs(nx, ny)
        return True

def bfs(z):
    global ans
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if array[i][j] == z:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for a, b in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx = x + a
            ny = y + b
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if array[nx][ny] > 0 and array[nx][ny] != z:
                ans = min(ans, dist[x][y])
                return

            if array[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])

cnt = 2

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1

for i in range(2, cnt):
    bfs(i)

print(ans)