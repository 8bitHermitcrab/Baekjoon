# 별 찍기 - 10

star = '***\n* *\n***'

# n = 3^k
# k = 3^n

n = int(input())
print(star*9, end='')

# if n // 3 == 0:
#     # (n/3)*(n/3) 크기의 정사각형
#     # n/3의 패턴
#     print(star*(n/3))
