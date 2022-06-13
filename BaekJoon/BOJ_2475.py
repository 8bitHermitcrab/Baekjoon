# 검증수

a, b, c, d, e = map(int, input().split())

total = (a**2)+(b**2)+(c**2)+(d**2)+(e**2)
answer = total % 10

print(answer)