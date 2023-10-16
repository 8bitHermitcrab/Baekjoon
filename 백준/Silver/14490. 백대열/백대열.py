n, m = map(int, input().split(':'))

def gcd(a, b):
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a

a = gcd(n, m)
print('%d:%d' %(n // a, m // a))