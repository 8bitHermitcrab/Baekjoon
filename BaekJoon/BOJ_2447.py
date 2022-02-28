# 별 찍기 - 10

N = int(input())
board = [[0 for i in range(N)] for i in range(N)]

# 별 찍는 함수
def draw_star(n):
    if n == 3:
        # 1행 = 3행 = [1, 1, 1]
        board[0][:3] = board[2][:3] = [1] * 3
        # 2행 = [1, 0, 1]
        board[1][:3] = [1, 0, 1]
        return

    a = n//3
    draw_star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            # a = n//3
            for k in range(a):
                # 핵심 아이디어
                board[a*i+k][a*j:a*(j+1)] = board[k][:a]

draw_star(N)

for i in board:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()


'''
star = ['***', '* *', '***']

# n = 3^k
# k = 3^n

# if n // 3 == 0:
#     # (n/3)*(n/3) 크기의 정사각형
#     # n/3의 패턴
#     print(star*(n/3))


https://study-all-night.tistory.com/5
'''