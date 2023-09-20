# 주유소

import sys
input = sys.stdin.readline

n = int(input())
way = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 첫번째 값 더하기
min_price = way[0] * cost[0]

# 가장 값이 싼 주유소
min_cost = cost[0]

for i in range(1, n-1):
    # 가장 싼 주유소가 현재 주유소보다 비싸면 바꾸기
    if cost[i] < min_cost:
        # 싼 주유소로 바꾸기
        min_cost = cost[i]
    min_price += min_cost * way[i]

print(min_price)


# https://jokerldg.github.io/algorithm/2021/03/16/gas-station.html