# 동전 0

n, k = map(int, input().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

count = 0

for i in reversed(range(n)):
    count += k//coin_list[i]
    print(f'k//coin_list[{i}] = {k//coin_list[i]}')
    k = k%coin_list[i]
    print(f'k%coin_list[{i}] = {k%coin_list[i]}')

print(count)
