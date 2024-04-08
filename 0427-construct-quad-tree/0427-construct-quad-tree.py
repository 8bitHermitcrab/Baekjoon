"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(a, b, c, d):
            z = o = 0
            for i in range(a, c + 1):
                for j in range(b, d + 1):
                    if grid[i][j] == 0:
                        z = 1
                    else:
                        o = 1
            leaf = z + o == 1
            val = leaf and o
            
            if leaf:
                return Node(grid[a][b], True)
            top_left = dfs(a, b, (a+c)//2, (b+d)//2)
            top_right = dfs(a, (b+d)//2+1, (a+c)//2, d)
            bot_left = dfs((a+c)//2+1, b, c, (b+d)//2)
            bot_right = dfs((a+c)//2+1, (b+d)//2+1, c, d)
            return Node(val, leaf, top_left, top_right, bot_left, bot_right)
        return dfs(0, 0, len(grid)-1, len(grid[0])-1)