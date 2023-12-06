# 이친수

n = int(input())

dp = [0, 1, 1]

for i in range(3, 91):
    answer = dp[i-1] + dp[i-2]
    dp.append(answer)

print(dp[n])