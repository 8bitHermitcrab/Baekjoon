# 기사단원의 무기

def solution(number, limit, power):
    divisors = [1]
    for i in range(2, number+1):
        cnt = 0

        for j in range(1, int(i**(1/2) + 1)):
            if i % j == 0:
                cnt += 1
                if j ** 2 != i:
                    cnt += 1

        if cnt > limit:
            cnt = power

        divisors.append(cnt)

    return sum(divisors)

print(solution(10, 3, 2))

# 참고 : https://haechichi.tistory.com/47

# 시간 초과
# def solution(number, limit, power):

#     def divisor(n):
#         cnt = 0

#         for i in range(1, n+1):
#             if n % i == 0:
#                 cnt += 1

#         return cnt
    
#     power_list = []
#     for i in range(1, number+1):
#         if divisor(i) > limit:
#             power_list.append(power)
        
#         else:
#             power_list.append(divisor(i))

#     return sum(power_list)