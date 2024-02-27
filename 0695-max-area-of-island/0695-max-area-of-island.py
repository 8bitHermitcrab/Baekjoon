class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        def bfs(i, j, row, col, grid, v):
            area = 1
            deq = deque()
            deq.append([i, j])
            v[i][j] = 1
            
            while deq:
                x, y = deq.popleft()
                for k in range(4):
                    new_x, new_y = x + dx[k], y + dy[k]
                    
                    if 0 <= new_x and new_x < row and 0 <= new_y and new_y < col and grid[new_x][new_y] == 1 and v[new_x][new_y] == 0:
                        v[new_x][new_y] = 1
                        deq.append([new_x, new_y])
                        area += 1
            return area
        
        row = len(grid)
        ans = 0
        col = len(grid[0])
        v = [0] * row
        
        for i in range(row):
            v[i] = [0] * col
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and v[i][j] == 0:
                    ans = max(ans, bfs(i, j, row, col, grid, v))
        return ans