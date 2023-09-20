# 소인수분해

n = int(input())

if n == 1:
    print('')

# 2부터 나누기
for i in range(2, n+1):
    if n % i == 0:
        # 해당 숫자로 나눌 수 없을 때까지 나누기
        while n % i == 0:
            print(i)
            n = n / i

# https://codinghani.tistory.com/5

'''
n = int(input())

i = 2

while n != 1:
    if n % 1 == 0:
        n = n / i
        print(i)
    else:
        i += 1


# https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-11653%EB%B2%88-%EC%86%8C%EC%9D%B8%EC%88%98%EB%B6%84%ED%95%B4-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''