n, m = map(int, input().split())

castle = []
x, y = 0, 0

for _ in range(n):
    castle.append(input())

for i in range(n):
    if 'X' not in castle[i]:
        x += 1

for j in range(m):
    if 'X' not in [castle[i][j] for i in range(n)]:
        y += 1

print(max(x, y))