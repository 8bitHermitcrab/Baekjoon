# 소수

m = int(input())
n = int(input())

# m~n 소수의 합
# 소수 체크
mn_list = list()

for num in range(m, n+1):
    error = 0
    if num > 1:
        for i in range(2, num): # 소수 탐색
            if num % i == 0:
                error += 1
                break
            # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            mn_list.append(num)

if len(mn_list) > 0:
    print(sum(mn_list))
    print(min(mn_list))
else:
    print(-1)


# https://ooyoung.tistory.com/93