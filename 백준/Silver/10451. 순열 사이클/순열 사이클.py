t = int(input())

def dfs(v):
    visited[v] = 1
    next = n_list[v]
    
    if visited[next] == 0:
        dfs(next)
    
    return

for _ in range(t):
    n = int(input())
    visited = [0] * (n + 1)
    n_list = list(map(int, input().split()))
    n_list.insert(0, 0)

    cnt = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1

    print(cnt)