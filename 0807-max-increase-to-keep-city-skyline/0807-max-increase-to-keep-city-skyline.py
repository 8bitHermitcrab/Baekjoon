class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        a = [max(h) for h in grid]
        b = [max(h) for h in zip(*grid)]
        
        for i, arr in enumerate(grid):
            for j, h in enumerate(arr):
                limit = min(a[i], b[j])
                if limit > h:
                    total += limit - h
        return total
        
        