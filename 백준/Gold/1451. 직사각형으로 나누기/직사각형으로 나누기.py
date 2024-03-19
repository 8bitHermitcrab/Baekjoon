n, m = map(int, input().split())

square = [[0 for _ in range(m + 1)]]

for _ in range(n):
    line_input = [0] + list(map(int, list(input())))
    square.append(line_input)
 
ans = 0
 
# 합을 저장할 리스트
s = [[0 for _ in range(m+1)] for _ in range(n+1)]
 
# 리스트 s는 입력받은 직사각형의 1,1부터 영역 내 모든 수의 합을 저장
for row in range(1, n + 1):
    for col in range(1, m + 1):
        s[row][col] = s[row - 1][col] + s[row][col - 1] - s[row - 1][col - 1] + square[row][col]
 
 
def sum_cal(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]
 
 
# 첫 번째 경우: 전체 직사각형을 세로로만 분할한 경우
for i in range(1, m-1):
    for j in range(i+1, m):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i+1, n, j)
        r3 = sum_cal(1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
 
# 두 번째 경우: 전체 직사각형을 가로로만 분할한 경우
for i in range(1, n-1):
    for j in range(i+1, n):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i+1, 1, j, m)
        r3 = sum_cal(j+1, 1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
# 세 번째 경우: 전체 세로 분할 후 우측 가로 분할한 경우
for i in range(1, m):
    for j in range(1, n):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i+1, j, m)
        r3 = sum_cal(j+1, i+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
# 네 번째 경우: 전체 세로 분할 후 좌측 가로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(i+1, 1, n, j)
        r3 = sum_cal(1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
# 다섯번 째 경우: 전체 가로 분할 후 하단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i+1, 1, n, j)
        r3 = sum_cal(i+1, j+1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
# 여섯번 째 경우: 전체 가로 분할 후 상단 세로 분할한 경우
for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(1, j+1, i, m)
        r3 = sum_cal(i+1, 1, n, m)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
print(ans)