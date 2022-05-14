# 최대공약수와 최소공배수


n = 3
m = 12

answer = []

def gcd(n, m):
    temp = m % n
    if temp != 0:
        m, n = n, temp
        return gcd(n, m)
    else:
        return n

lcm = (m*n / gcd(n, m))

answer = [gcd(n, m), int(lcm)]

print(answer)

'''
# 최대공약수 : gcd
for i in range(min(n, m), 0 -1):
    if n % i == 0 and m % i == 0:
        gcd = i
        answer.append(gcd)

# 최소공배수 : lcm
for i in range(max(n, m), (n*m)+1):
    if i % n == 0 and i % m == 0:
        lcm = i
        answer.append(lcm)
'''

# https://codingpractices.tistory.com/34
# https://velog.io/@richeberry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4python-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98