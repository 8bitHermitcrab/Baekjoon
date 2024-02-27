# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        next_lev = deque([root])
        
        while root and next_lev:
            curr_lev = next_lev
            next_lev = deque()
            levels.append([])
            
            for node in curr_lev:
                levels[-1].append(node.val)
                
                if node.left:
                    next_lev.append(node.left)
                if node.right:
                    next_lev.append(node.right)
    
        sum_lev = [sum(i) / len(i) for i in levels]
        return sum_lev