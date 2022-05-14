# 하샤드 수

x = 234

answer = ''

list_x = list(str(x))
sum_num = 0
print(list_x)

for i in range(len(list_x)):
    sum_num += int(list_x[i])
    print(sum_num)
    if x % sum_num == 0:
        answer = True
    else:
        answer = False


# https://wooaoe.tistory.com/73