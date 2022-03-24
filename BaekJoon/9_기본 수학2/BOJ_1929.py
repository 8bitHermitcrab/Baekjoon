# 소수 구하기

m, n = map(int, input().split())

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for i in range(m, n+1):
    if isPrime(i):
        print(i)


# https://deokkk9.tistory.com/17

'''
m, n = map(int, input().split())

num_list = []

for i in range(m, n+1):
    if i > 1:
        for j in range(2, i+1):
            if i % j != 0:
                num_list.append(i)
print(num_list[i])
'''
