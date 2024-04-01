import sys

input = sys.stdin.readline

r, c = map(int, input().split())
array = []
for _ in range(r):
    array.append(list(input()))
ans = 0
alphabet = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not array[nx][ny] in alphabet:
            alphabet.add(array[nx][ny])
            dfs(nx, ny, cnt+1)
            alphabet.remove(array[nx][ny])
alphabet.add(array[0][0])
dfs(0, 0, 1)
print(ans)