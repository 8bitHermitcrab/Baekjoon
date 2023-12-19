n = int(input())

a1 = list(map(int, input().split()))
a2 = a1[::-1]

s1 = [1 for _ in range(n)]
s2 = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a1[i] > a1[j]:
            s1[i] = max(s1[i], s1[j] + 1)
        if a2[i] > a2[j]:
            s2[i] = max(s2[i], s2[j] + 1)

result = [0 for _ in range(n)]

for i in range(n):
    result[i] = s1[i] + s2[n - i - 1] - 1

print(max(result))