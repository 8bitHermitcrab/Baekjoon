# 정수 제곱근 판별

# import math
# math.sqrt(2)

n = 3

r_n = n ** (1/2)

if r_n == int(r_n):
    answer = (r_n + 1)*(r_n + 1)
else : 
    answer = -1

print(r_n)
print(answer)


# https://needneo.tistory.com/77