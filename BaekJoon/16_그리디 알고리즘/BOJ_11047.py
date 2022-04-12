# 동전 0

n, k = map(int, input().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

count = 0

for i in reversed(range(n)):
    # 나누기 연산 정수 부분
    count += k//coin_list[i]
    print(f'k//coin_list[{i}] = {k//coin_list[i]}')
    # 나누기 연산 나머지 부분
    k = k%coin_list[i]
    print(f'k%coin_list[{i}] = {k%coin_list[i]}')

print(count)


# https://god-gil.tistory.com/64