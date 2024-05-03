def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    temp = set()
    
    while True:
        
        for i in range(m-1) :
            for j in range(n-1):
                t = board[i][j]
                if ( t == [] ) :
                    continue
                else :
                    if( board[i][j+1] == t and board[i+1][j] == t and board[i+1][j+1] == t) :
                        temp.add((i,j))
                        temp.add((i,j+1))
                        temp.add((i+1,j))
                        temp.add((i+1,j+1))
                        
        if temp :
            answer += len(temp)
            for i, j in temp :
                board[i][j] = []
            temp = set()
        else :
            break
        
        while True :
            moved = 0
            for i in range(m - 1) :
                for j in range(n) :
                    if( board[i][j] and board[i+1][j] == [] ) :
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        moved = 1
            if ( moved == 0 ):
                break
    
    return answer