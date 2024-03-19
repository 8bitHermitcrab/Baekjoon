class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        max_sum = 0
      
        for row in range(1, num_row - 1):
            for col in range(1, num_col - 1):
                hourglass_sum = grid[row - 1][col - 1] + grid[row - 1][col] + grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1] + grid[row + 1][col] + grid[row + 1][col + 1]
                max_sum = max(max_sum, hourglass_sum)
        return max_sum