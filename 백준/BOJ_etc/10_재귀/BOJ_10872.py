# 팩토리얼

n = int(input())

if n == 0:
    print(1)
else:
    m = n + 1
    result = 1
    for i in range(1, m):
        result *= i

    print(result)
