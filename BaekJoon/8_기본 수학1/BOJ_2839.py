# 설탕 배달

# n 킬로그램
n = int(input())

bag = [5, 3]
count = 0

while n >= 0:
    # 5의 배수일 때
    if n % bag[0] == 0:
        count += (n // 5)
        print(count)
        break
    n -= 3
    # 5의 배수가 될 때까지 설탕-3, 봉지+1
    count += 1
else:
    print(-1)

'''
b3 = 3
b5 = 5
count = 0

for _ in range(n):
    result = n // 5
    n - result
    count += 1


    if result == 0:
        print(count)
    else:
        print(-1)
'''

# https://ooyoung.tistory.com/81