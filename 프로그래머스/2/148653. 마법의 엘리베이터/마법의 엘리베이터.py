def solution(storey):
    answer = []
    
    def dfs(st, count):
        if st == 0:
            answer.append(count)
            return
        
        one = st % 10
        up, down = 10 - one, one

        if up < down:
            dfs(st // 10 + 1, count + up)
            
        elif down < up:
            dfs(st //10, count + down)
            
        else:
            for i in range(2):
                dfs(st // 10 + i, count + up)
    
    dfs(storey, 0)
    return min(answer)