n = int(input())
dist = []
result = []

for i in range(n):
    dist.append(list(map(int, input().split())))

def dfs(idx, cnt, min_dist, start):
    if cnt == n:
        if dist[idx][start] != 0:
            min_dist += dist[idx][start]
            result.append(min_dist)
        return
    visited[start] = True

    for i in range(n):
        if visited[i] == False:
            if dist[idx][i] != 0:
                visited[i] = True
                min_dist += dist[idx][i]
                dfs(i, cnt+1, min_dist, start)
                visited[i] = False
                min_dist -= dist[idx][i]

for i in range(n):
    visited = [False] * n
    dfs(i, 1, 0, i)

print(min(result))