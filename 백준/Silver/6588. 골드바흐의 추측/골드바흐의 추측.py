import sys
input = sys.stdin.readline

num = [True] * 1000001

for i in range(2, int(len(num) ** 0.5) + 1):
    if num[i]:
        for j in range(2*i, 1000001, i):
            num[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    
    else:
        for i in range(n-3, 2, -2):
            if num[i] == True and num[n - i] == True:
                print(f'{n} = {n-i} + {i}')
                break