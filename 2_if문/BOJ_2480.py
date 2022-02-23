# 주사위 세개

dice1, dice2, dice3 = map(int, input().split())
price = 0

# 3개가 같을 때
if dice1 == dice2 and dice1 == dice3:
    price = 10000 + (dice1 * 1000)
# 2개가 같을 때
elif dice1 == dice2 and dice1 != dice3:
    price = 1000 + (dice1 * 100)
elif dice1 != dice2 and dice2 == dice3:
    price = 1000 + (dice2 * 100)
elif dice1 == dice3 and dice2 != dice3:
    price = 1000 + (dice1 * 100)
# 모두 다를 때
else:
    # dice1가 클 때
    if dice1 > dice2 and dice1 > dice3:
        price = dice1 * 100
    # dice2가 클 때
    elif dice2 > dice1 and dice2 > dice3:
        price = dice2 * 100
    # dice3가 클 때
    elif dice3 > dice1 and dice3 > dice2:
        price = dice3 * 100


print(price)


