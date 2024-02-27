class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        regions = {}
        
        def find(x):
            y = regions.get(x, x)
            
            if y != x:
                regions[x] = y
                y = find(y)
            return y
        
        def union(x, y):
            regions[find(x)] = find(y)
            
        size = len(grid)
        
        for i in range(size):
            for j in range(size):
                if i > 0:
                    union((i-1, j, 'S'), (i, j, 'N'))
                
                if j > 0:
                    union((i, j-1, 'E'), (i, j, 'W'))
                    
                if grid[i][j] != "/":
                    union((i, j, 'N'), (i, j, 'E'))
                    union((i, j, 'S'), (i, j, 'W'))
                
                if grid[i][j] != "\\":
                    union((i, j, 'N'), (i, j, 'W'))
                    union((i, j, 'S'), (i, j, 'E'))
        return len(set(map(find, regions)))
        