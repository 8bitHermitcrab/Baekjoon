
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())

print(graph)

# dx = [1, -1, 0, 0, 1, -1, 1, -1]
# dy = [0, 0, 1, -1, 1, -1, -1, 1]

# def dfs(x, y):
#     if land[x][y] == 0:
#         return 0
    
#     land[x][y] = 0
#     for i in range(8):
#         nx, ny = x + dx[i], y + dy[i]

#         if nx < 0 or nx > (h - 1) or ny < 0 or ny > (w - 1):
#             continue

#         if land[nx][ny] == 0:
#             continue

#         dfs(nx, ny)

#     return 1

# while True:
#     w, h = map(int, input().split())

#     if w == h == 0:
#         break
    
#     land = [list(map(int, input().split())) for _ in range(h)]

#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             cnt += dfs(i, j)

#     print(cnt)
