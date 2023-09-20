# 알고리즘 수업 - 깊이 우선 탐색 1

# DFS

# 정점 N개
# 간선 M개
# 정점 R에서 시작 - 방문순서 출력

N, M, R = map(int, input().split())

grapth = [[] for _ in range(N+1)]
path = []
result = [0] * (N+1)
visited = [-1]*(N+1)

for _ in range(M):
    



def dfs(V, E, R): # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] = 1 # 시작 정점 R 방문




