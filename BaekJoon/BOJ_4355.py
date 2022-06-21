# 서로소


import sys, time

# start_t = time.time()
answer = []

# 유클리드 호제법
# def gcd(a, b):
#     if a%b == 0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         return gcd(b, a%b)

result = 0
c = 0

# 최대공약수
def gcd(a, b):
    if a%b != 0:
        return b
    else:
        return gcd(b, a%b)

# 최소공배수
def union():
    t = 1
    for a in range(100001):
        d = gcd(max(union(a), t), min(union(a), t))
        t = t / d * a
    return c / t

# 오일러(p^k) = p^k * (1-1/p) = p^(k-1) * (p-1)
def Euler(n):
    cnt = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            cnt += 1
    return cnt

for i in range(10):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
print(Euler(n), sep='\n')

# end_t = time.time() - start_t
# print(end_t)



'''import time, math

# 소수 판별
def isPrime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0 :
            return False
    return True

# 소수 찾기
def findPrimes(n):
    primes = []
    for i in range(2, n+1):  # for i in range(2, (n//2)+1) 로 개선 가능
        if isPrime(i):
            primes.append(i)
    return primes

print('소수 리스트', findPrimes(30))

# 소인수 분해 1
def factorize(n):
    factors = []
    primes = findPrimes(n)  # n의 소수 리스트를 추출
    for i in primes:
        while (n % i == 0):  # 소수 중 나누어 떨어지는(약수) 수를 찾는다
            factors.append(i)
            n = n // i
    return factors

print('소인수분해 결과', factorize(30))

# 효율적인 소인수 분해
def factorize2(n):
    factor = 2 #시작 소수 지정
    factors = []
    while (factor**2 <= n):  # 에라토스테네스를 떠올리며,, 즉 루트n까지 실행
        while (n % factor == 0):  # 소수로 나누어 떨어지면(= 즉 약수면)
            factors.append(factor)  # 리스트에 추가
            n = n // factor  # n을 몫으로 변경
        factor += 1
    if n > 1 : # 1보다 크고 factor**2(4)보다 작은 경우 n은 소수임으로 append -> 2,3 경우
        factors.append(n)

print('효율적인 소인수분해 결과', factorize2(30))


start_t = time.time()
print('효율적인 소인수분해 결과', factorize2(4643623532532))
end_t = time.time() - start_t
print(end_t)

start_t = time.time()
print('소인수분해 결과', factorize(4643623532532))
end_t = time.time() - start_t
print(end_t)
'''