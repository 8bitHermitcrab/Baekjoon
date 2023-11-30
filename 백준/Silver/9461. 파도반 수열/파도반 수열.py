t = int(input())

n = [int(input()) for _ in range(t)]

p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, max(n)+1):
    p.append(p[i-1] + p[i-5])

for i in n:
    print(p[i])