class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        
        trans_grid = zip(*grid)
        sum_max_values = sum(max(column) for column in trans_grid)
        return sum_max_values