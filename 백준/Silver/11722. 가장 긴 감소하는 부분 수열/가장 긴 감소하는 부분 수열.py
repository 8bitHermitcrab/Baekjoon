a = int(input())
n = list(map(int, input().split()))

dp = [1] * a

for i in range(a):
    for j in range(i):
        if n[j] > n[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))