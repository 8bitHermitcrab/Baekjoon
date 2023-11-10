n = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
    cnt += n // coin
    n %= coin

print(cnt)