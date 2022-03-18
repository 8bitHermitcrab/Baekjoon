# 분수 찾기

n = int(input())

# 사선 라인
line = 0
# 입력 숫자의 라인에서 가장 큰 수
max_n = 0

while n > max_n:
    line += 1
    max_n += line

gap = max_n - n

# 사선 라인이 짝수번째일 때
if line % 2 == 0:
    # 분자
    top = line - gap
    # 분모
    under = gap + 1
# 사선 라인이 홀수번째일 때
else :
    # 분자
    top = gap + 1
    # 분모
    under = line - gap

print(f'{top}/{under}')


'''
for i in range(n):
    result = n-1
    if n    
print()

# https://ooyoung.tistory.com/84
'''