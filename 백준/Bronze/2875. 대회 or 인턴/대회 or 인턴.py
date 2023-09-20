# 대회 or 인턴

n, m, k = map(int, input().split())

# 인턴십 제외, 대회 참여 가능
for i in range(k):
    if n // 2 >= m:
        n -= 1
    else:
        m -= 1

print(min(n//2, m))