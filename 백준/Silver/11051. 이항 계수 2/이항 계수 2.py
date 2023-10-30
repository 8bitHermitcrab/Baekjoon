n, k = map(int, input().split())

result = 1
for _ in range(k):
    result *= n
    n -= 1

d = 1
for i in range(2, k+1):
    d *= i

print((result // d) % 10007)