class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = [0] * n

        for i in range(m):
            row = grid[i]
            if row[0] == 0:
                for j in range(n):
                    if row[j] == 0:
                        row[j] = 1
                        cnt[j] += 1
                    else:
                        row[j] = 0

            else:
                for j in range(n):
                    if row[j] == 1:
                        cnt[j] += 1

        for j in range(n):
            if cnt[j] < m // 2 + m % 2:
                for i in range(m):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        
        result = 0
        for row in grid:
            temp = int(''.join([str(x) for x in row]), 2)
            result += temp
        return result