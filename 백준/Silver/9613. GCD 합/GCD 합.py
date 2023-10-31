import math

t = int(input())

for _ in range(t):
    n = list(map(int, input().split()))


    total = 0
    for i in range(1, len(n)):
        for j in range(i+1, len(n)):
            total += math.gcd(n[i], n[j])

    print(total)