class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        land = 0
        neighbor = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land += 1
                    if i + 1 < m and grid[i + 1][j] == 1:
                        neighbor += 1
                    if j + 1 < n and grid[i][j + 1] == 1:
                        neighbor += 1

        return land * 4 - neighbor * 2