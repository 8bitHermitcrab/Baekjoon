import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
    global cnt
    visited[n] = True
    cycle_list.append(n)

    if visited[arr[n]] == True:
        if arr[n] in cycle_list:
            cnt -= len(cycle_list[cycle_list.index(arr[n]):])
        return
    else:
        dfs(arr[n])

t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = [0]
    arr.extend([int(x) for x in input().rstrip().split()])
    visited = [False] * (n + 1)
    cnt = n

    for i in range(1, n+1):
        if not visited[i]:
            cycle_list = []
            dfs(i)

    print(cnt)