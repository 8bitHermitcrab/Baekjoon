
money = int(input())
# cost = map(int, input().split())
money_dict = dict()

# 의뢰받은 금액 : money
count = 0
# 6종류 동전의 생산 단가
coins = [500, 100, 50, 10, 5, 1]
costs = [600, 200, 100, 20, 11, 2]
for coin in coins:
    count = money // coin
    money %= coin
    money_dict[coin] = count
# print(money_dict)

count_list = []
count_list = money_dict.values()

answer = 0

for i in range(len(coins)):
    for value in money_dict.values():
        answer += value * coins[i]

print(answer)

""" for cost in costs:
    count = money // cost
    money %= cost
    cost_dict[cost] = count 
print(cost_dict) """