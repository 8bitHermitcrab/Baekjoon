# 숫자의 개수

a, b, c = [int(input()) for _ in range(3)]

num = list(str(a * b * c))

for i in range(10):
    print(num.count(str(i)))
