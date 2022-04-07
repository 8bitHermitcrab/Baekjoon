# 체스판 다시 칠하기

n, m = map(int, input().split())

board = []
chessboard = []

# WB입력 넣기
for _ in range(n):
    board.append(input())

# 8x8로 자르기
for i in range(n-7):
    for j in range(m-7):
        idx1 = 0
        idx2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8): # 8x8 범위를 B와 W로 번갈아가면서 검사
                if (b+a)%2 == 0:
                    if board[a][b] != 'W':
                        idx1 += 1
                    if board[a][b] != 'B':
                        idx2 += 1
                else:
                    if board[a][b] != 'B':
                        idx1 += 1
                    if board[a][b] != 'W':
                        idx2 += 1
        chessboard.append(idx1) # W로 시작했을 때 칠해야 할 부분
        chessboard.append(idx2) # B로 시작했을 때 칠해야 할 부분

# 칠해야하는 개수의 최소값
print(min(chessboard))


# https://leejunggae.tistory.com/14